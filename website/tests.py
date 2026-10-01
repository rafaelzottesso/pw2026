from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from datetime import datetime

from .filters import JogoFilter, ModalidadeFilter
from .models import Campus, Campeonato, Fase, Inscricao, Jogador, Jogo, Modalidade


class ListingFilterTests(TestCase):
	def setUp(self):
		user_model = get_user_model()
		self.user = user_model.objects.create_user(
			username="organizador", password="senha-teste"
		)
		self.campus = Campus.objects.create(nome="Campus Central")
		self.modalidade = Modalidade.objects.create(nome="Basquete")
		self.fase = Fase.objects.create(
			nome="Final", quantidade_jogos=1, sequencia=1
		)
		self.campeonato = Campeonato.objects.create(
			nome="Copa de Teste",
			categoria="Adulto",
			data_inicio=timezone.make_aware(datetime(2026, 5, 1, 12)),
			data_limite_inscricao=timezone.make_aware(datetime(2026, 5, 9, 12)),
			campus=self.campus,
			cadastrado_por=self.user,
		)
		self.time_1 = Inscricao.objects.create(
			nome_time="Alpha Esports",
			campeonato=self.campeonato,
			modalidade=self.modalidade,
			inscrito_por=self.user,
		)
		self.time_2 = Inscricao.objects.create(
			nome_time="Beta Esports",
			campeonato=self.campeonato,
			modalidade=self.modalidade,
			inscrito_por=self.user,
		)

	def criar_jogo(self, data_hora):
		return Jogo.objects.create(
			time_1=self.time_1,
			time_2=self.time_2,
			data_hora=data_hora,
			etapa=self.fase,
			modalidade=self.modalidade,
			cadastrado_por=self.user,
		)

	def test_text_filter_finds_partial_case_insensitive_value(self):
		filterset = ModalidadeFilter(
			data={"nome__icontains": "sQuEt"},
			queryset=Modalidade.objects.all(),
		)

		self.assertTrue(filterset.is_valid(), filterset.errors)
		self.assertQuerySetEqual(filterset.qs, [self.modalidade])

	def test_datetime_filter_includes_the_entire_end_date(self):
		ultimo_dia = self.criar_jogo(
			timezone.make_aware(datetime(2026, 5, 10, 23, 59, 59))
		)
		proximo_dia = self.criar_jogo(
			timezone.make_aware(datetime(2026, 5, 11, 0, 0, 0))
		)
		filterset = JogoFilter(
			data={
				"data_hora__date__gte": "2026-05-10",
				"data_hora__date__lte": "2026-05-10",
			},
			queryset=Jogo.objects.all(),
		)

		self.assertTrue(filterset.is_valid(), filterset.errors)
		self.assertIn(ultimo_dia, filterset.qs)
		self.assertNotIn(proximo_dia, filterset.qs)

	def test_pagination_keeps_filter_query_parameters(self):
		user_model = get_user_model()
		for index in range(4):
			jogador_user = user_model.objects.create_user(
				username=f"jogador{index}"
			)
			Jogador.objects.create(
				nome=f"Alpha Jogador {index}",
				campus=self.campus,
				usuario=jogador_user,
			)

		self.client.force_login(self.user)
		response = self.client.get(
			reverse("jogador_list"),
			{"nome__icontains": "Alpha", "page": 2},
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context["page_obj"].number, 2)
		self.assertContains(response, "Listagem de Jogadores")
		self.assertContains(response, "Novo Jogador")
		self.assertContains(response, "Filtro")
		self.assertContains(response, "nome__icontains=Alpha")
		self.assertContains(response, "page=1")
