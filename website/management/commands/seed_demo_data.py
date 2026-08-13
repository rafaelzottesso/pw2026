from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from website.models import Campeonato, Inscricao, Jogador, Jogo
from website.models import Campus, Fase, Modalidade


class Command(BaseCommand):
    help = "Cria dados ficticios para demonstracao do sistema."

    def handle(self, *args, **options):
        with transaction.atomic():
            self.create_reference_data()
            users = self.create_users()
            players = self.create_players(users)
            championships = self.create_championships(users)
            registrations = self.create_registrations(championships, players, users)
            games = self.create_games(championships, registrations, users)

        self.stdout.write(self.style.SUCCESS(
            "Dados criados/atualizados: "
            f"{len(users)} usuarios, {len(players)} jogadores, "
            f"{len(championships)} campeonatos, {len(registrations)} inscricoes "
            f"e {len(games)} jogos."
        ))
        self.stdout.write(
            "Senha inicial dos usuarios ficticios novos: Arena@2026"
        )

    def create_users(self):
        user_model = get_user_model()
        users = {}
        user_data = [
            ("seed.organizador", "Organizador", "Demo", "seed.organizador@example.com"),
            ("ana.silva", "Ana", "Silva", "ana.silva@example.com"),
            ("bruno.costa", "Bruno", "Costa", "bruno.costa@example.com"),
            ("carla.mendes", "Carla", "Mendes", "carla.mendes@example.com"),
            ("diego.oliveira", "Diego", "Oliveira", "diego.oliveira@example.com"),
            ("elisa.rocha", "Elisa", "Rocha", "elisa.rocha@example.com"),
            ("felipe.santos", "Felipe", "Santos", "felipe.santos@example.com"),
            ("gabriela.alves", "Gabriela", "Alves", "gabriela.alves@example.com"),
            ("henrique.lima", "Henrique", "Lima", "henrique.lima@example.com"),
            ("isabela.farias", "Isabela", "Farias", "isabela.farias@example.com"),
            ("joao.martins", "Joao", "Martins", "joao.martins@example.com"),
            ("karina.nunes", "Karina", "Nunes", "karina.nunes@example.com"),
            ("lucas.pereira", "Lucas", "Pereira", "lucas.pereira@example.com"),
        ]

        for username, first_name, last_name, email in user_data:
            user, created = user_model.objects.get_or_create(
                username=username,
                defaults={
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                },
            )
            if created:
                user.set_password("Arena@2026")
                user.save(update_fields=["password"])
            users[username] = user

        return users

    def create_reference_data(self):
        for campus_name in ["Paranavaí", "Curitiba", "Umuarama", "Toledo"]:
            Campus.objects.get_or_create(nome=campus_name)

        for modality_name in ["CS 2", "LOL", "Fifa", "Xadrez"]:
            Modalidade.objects.get_or_create(nome=modality_name)

        phase_data = [
            ("Oitavas de final", 8, 1),
            ("Quartas de final", 4, 2),
            ("Semifinal", 2, 3),
            ("Final", 1, 4),
        ]
        for name, games_quantity, sequence in phase_data:
            Fase.objects.get_or_create(
                sequencia=sequence,
                defaults={"nome": name, "quantidade_jogos": games_quantity},
            )

    def create_players(self, users):
        campuses = list(Campus.objects.order_by("id"))
        if len(campuses) < 4:
            raise ValueError("Cadastre pelo menos quatro campi antes de executar este comando.")

        players = {}
        player_data = [
            ("ana.silva", "Ana Silva", "44991000001", campuses[0]),
            ("bruno.costa", "Bruno Costa", "44991000002", campuses[1]),
            ("carla.mendes", "Carla Mendes", "44991000003", campuses[2]),
            ("diego.oliveira", "Diego Oliveira", "44991000004", campuses[3]),
            ("elisa.rocha", "Elisa Rocha", "44991000005", campuses[0]),
            ("felipe.santos", "Felipe Santos", "44991000006", campuses[1]),
            ("gabriela.alves", "Gabriela Alves", "44991000007", campuses[2]),
            ("henrique.lima", "Henrique Lima", "44991000008", campuses[3]),
            ("isabela.farias", "Isabela Farias", "44991000009", campuses[0]),
            ("joao.martins", "Joao Martins", "44991000010", campuses[1]),
            ("karina.nunes", "Karina Nunes", "44991000011", campuses[2]),
            ("lucas.pereira", "Lucas Pereira", "44991000012", campuses[3]),
        ]

        for username, name, phone, campus in player_data:
            player, _ = Jogador.objects.update_or_create(
                usuario=users[username],
                defaults={"nome": name, "telefone": phone, "campus": campus},
            )
            players[username] = player

        return players

    def create_championships(self, users):
        campuses = list(Campus.objects.order_by("id"))
        modalities = list(Modalidade.objects.order_by("id"))
        if len(campuses) < 3 or len(modalities) < 3:
            raise ValueError("Cadastre pelo menos tres campi e tres modalidades antes de executar este comando.")

        start = timezone.now() + timedelta(days=10)
        championship_data = [
            ("Copa Academica de Inverno", "Intermediario", campuses[0], [modalities[0], modalities[1]], start),
            ("Liga Universitaria de Primavera", "Avancado", campuses[1], [modalities[1], modalities[2]], start + timedelta(days=30)),
            ("Desafio Regional de Estrategia", "Aberto", campuses[2], [modalities[0], modalities[3]], start + timedelta(days=60)),
        ]

        championships = {}
        for index, (name, category, campus, championship_modalities, date_start) in enumerate(championship_data):
            championship, _ = Campeonato.objects.update_or_create(
                nome=name,
                defaults={
                    "categoria": category,
                    "data_inicio": date_start,
                    "data_limite_inscricao": date_start - timedelta(days=3),
                    "campus": campus,
                    "cadastrado_por": users["seed.organizador"],
                },
            )
            championship.modalidades.set(championship_modalities)
            championships[index] = championship

        return championships

    def create_registrations(self, championships, players, users):
        modalities = list(Modalidade.objects.order_by("id"))
        player_names = list(players)
        registrations = {}
        team_data = [
            (0, "Equipe Aurora", 0, [0, 1], True),
            (0, "Equipe Nebula", 1, [2, 3], True),
            (0, "Equipe Orbit", 0, [4, 5], False),
            (0, "Equipe Zenith", 1, [6, 7], True),
            (1, "Equipe Vanguarda", 1, [1, 8], True),
            (1, "Equipe Prisma", 2, [3, 9], True),
            (1, "Equipe Horizonte", 2, [5, 10], False),
            (1, "Equipe Eclipse", 1, [7, 11], True),
            (2, "Equipe Tabuleiro", 3, [0, 6], True),
            (2, "Equipe Gambito", 3, [2, 8], True),
            (2, "Equipe Torre", 0, [4, 10], False),
            (2, "Equipe Rei", 3, [9, 11], True),
        ]

        for championship_index, team_name, modality_index, player_indexes, confirmed in team_data:
            championship = championships[championship_index]
            modality = modalities[modality_index]
            registration, _ = Inscricao.objects.update_or_create(
                nome_time=team_name,
                campeonato=championship,
                defaults={
                    "modalidade": modality,
                    "confirmada": confirmed,
                    "confirmada_em": timezone.now() if confirmed else None,
                    "inscrito_por": users[player_names[player_indexes[0]]],
                },
            )
            registration.jogadores.set(players[player_names[index]] for index in player_indexes)
            registrations[team_name] = registration

        return registrations

    def create_games(self, championships, registrations, users):
        phases = {phase.sequencia: phase for phase in Fase.objects.all()}
        if not {3, 4}.issubset(phases):
            raise ValueError("Cadastre as fases Semifinal e Final antes de executar este comando.")

        games = []
        game_data = [
            ("Copa Academica de Inverno", "Equipe Aurora", "Equipe Nebula", 3, "2-1", "Equipe Aurora", 2),
            ("Copa Academica de Inverno", "Equipe Orbit", "Equipe Zenith", 3, "0-2", "Equipe Zenith", 3),
            ("Copa Academica de Inverno", "Equipe Aurora", "Equipe Zenith", 4, "2-0", "Equipe Aurora", 4),
            ("Liga Universitaria de Primavera", "Equipe Vanguarda", "Equipe Prisma", 3, "1-2", "Equipe Prisma", 5),
            ("Liga Universitaria de Primavera", "Equipe Horizonte", "Equipe Eclipse", 3, None, None, 6),
            ("Liga Universitaria de Primavera", "Equipe Prisma", "Equipe Eclipse", 4, None, None, 7),
            ("Desafio Regional de Estrategia", "Equipe Tabuleiro", "Equipe Gambito", 3, "1-0", "Equipe Tabuleiro", 8),
            ("Desafio Regional de Estrategia", "Equipe Torre", "Equipe Rei", 3, None, None, 9),
            ("Desafio Regional de Estrategia", "Equipe Tabuleiro", "Equipe Torre", 4, None, None, 10),
        ]

        for championship_name, team_1_name, team_2_name, phase_sequence, result, winner_name, day_offset in game_data:
            championship = Campeonato.objects.get(nome=championship_name)
            time_1 = registrations[team_1_name]
            time_2 = registrations[team_2_name]
            winner = registrations.get(winner_name) if winner_name else None
            game, _ = Jogo.objects.update_or_create(
                cadastrado_por=users["seed.organizador"],
                time_1=time_1,
                time_2=time_2,
                etapa=phases[phase_sequence],
                defaults={
                    "data_hora": championship.data_inicio + timedelta(days=day_offset),
                    "modalidade": time_1.modalidade,
                    "vencedor": winner,
                    "resultado": result,
                },
            )
            games.append(game)

        return games
