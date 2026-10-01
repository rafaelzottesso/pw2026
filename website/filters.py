import django_filters
from django import forms

from .models import (
    Campus,
    Campeonato,
    Fase,
    Inscricao,
    Jogador,
    Jogo,
    Modalidade,
)


def date_input():
    return forms.DateInput(attrs={"type": "date"})


class ModalidadeFilter(django_filters.FilterSet):
    nome__icontains = django_filters.CharFilter(
        field_name="nome", lookup_expr="icontains", label="Nome contém"
    )

    class Meta:
        model = Modalidade
        fields = {"nome": ["icontains"]}


class FaseFilter(django_filters.FilterSet):
    nome__icontains = django_filters.CharFilter(
        field_name="nome", lookup_expr="icontains", label="Nome contém"
    )
    quantidade_jogos__gte = django_filters.NumberFilter(
        field_name="quantidade_jogos", lookup_expr="gte", label="Mínimo de jogos"
    )
    quantidade_jogos__lte = django_filters.NumberFilter(
        field_name="quantidade_jogos", lookup_expr="lte", label="Máximo de jogos"
    )
    sequencia__gte = django_filters.NumberFilter(
        field_name="sequencia", lookup_expr="gte", label="Sequência a partir de"
    )
    sequencia__lte = django_filters.NumberFilter(
        field_name="sequencia", lookup_expr="lte", label="Sequência até"
    )

    class Meta:
        model = Fase
        fields = {
            "nome": ["icontains"],
            "quantidade_jogos": ["gte", "lte"],
            "sequencia": ["gte", "lte"],
        }


class JogadorFilter(django_filters.FilterSet):
    nome__icontains = django_filters.CharFilter(
        field_name="nome", lookup_expr="icontains", label="Nome contém"
    )
    telefone__icontains = django_filters.CharFilter(
        field_name="telefone", lookup_expr="icontains", label="Telefone contém"
    )
    campus = django_filters.ModelChoiceFilter(
        queryset=Campus.objects.order_by("nome"), label="Campus"
    )

    class Meta:
        model = Jogador
        fields = {
            "nome": ["icontains"],
            "telefone": ["icontains"],
            "campus": ["exact"],
        }


class CampeonatoFilter(django_filters.FilterSet):
    nome__icontains = django_filters.CharFilter(
        field_name="nome", lookup_expr="icontains", label="Nome contém"
    )
    categoria__icontains = django_filters.CharFilter(
        field_name="categoria", lookup_expr="icontains", label="Categoria contém"
    )
    campus = django_filters.ModelChoiceFilter(
        queryset=Campus.objects.order_by("nome"), label="Campus"
    )
    data_inicio__date__gte = django_filters.DateFilter(
        field_name="data_inicio",
        lookup_expr="date__gte",
        label="Início a partir de",
        widget=date_input(),
    )
    data_inicio__date__lte = django_filters.DateFilter(
        field_name="data_inicio",
        lookup_expr="date__lte",
        label="Início até",
        widget=date_input(),
    )
    data_limite_inscricao__date__gte = django_filters.DateFilter(
        field_name="data_limite_inscricao",
        lookup_expr="date__gte",
        label="Limite de inscrição a partir de",
        widget=date_input(),
    )
    data_limite_inscricao__date__lte = django_filters.DateFilter(
        field_name="data_limite_inscricao",
        lookup_expr="date__lte",
        label="Limite de inscrição até",
        widget=date_input(),
    )

    class Meta:
        model = Campeonato
        fields = {
            "nome": ["icontains"],
            "categoria": ["icontains"],
            "campus": ["exact"],
            "data_inicio": ["date__gte", "date__lte"],
            "data_limite_inscricao": ["date__gte", "date__lte"],
        }


class CampusFilter(django_filters.FilterSet):
    nome__icontains = django_filters.CharFilter(
        field_name="nome", lookup_expr="icontains", label="Nome contém"
    )

    class Meta:
        model = Campus
        fields = {"nome": ["icontains"]}


class InscricaoFilter(django_filters.FilterSet):
    nome_time__icontains = django_filters.CharFilter(
        field_name="nome_time", lookup_expr="icontains", label="Nome do time contém"
    )
    campeonato__nome__icontains = django_filters.CharFilter(
        field_name="campeonato__nome",
        lookup_expr="icontains",
        label="Campeonato contém",
    )
    modalidade = django_filters.ModelChoiceFilter(
        queryset=Modalidade.objects.order_by("nome"), label="Modalidade"
    )
    confirmada = django_filters.BooleanFilter(label="Confirmada")
    inscrito_em__date__gte = django_filters.DateFilter(
        field_name="inscrito_em",
        lookup_expr="date__gte",
        label="Inscrição a partir de",
        widget=date_input(),
    )
    inscrito_em__date__lte = django_filters.DateFilter(
        field_name="inscrito_em",
        lookup_expr="date__lte",
        label="Inscrição até",
        widget=date_input(),
    )

    class Meta:
        model = Inscricao
        fields = {
            "nome_time": ["icontains"],
            "campeonato__nome": ["icontains"],
            "modalidade": ["exact"],
            "confirmada": ["exact"],
            "inscrito_em": ["date__gte", "date__lte"],
        }


class JogoFilter(django_filters.FilterSet):
    time_1__nome_time__icontains = django_filters.CharFilter(
        field_name="time_1__nome_time",
        lookup_expr="icontains",
        label="Equipe 1 contém",
    )
    time_2__nome_time__icontains = django_filters.CharFilter(
        field_name="time_2__nome_time",
        lookup_expr="icontains",
        label="Equipe 2 contém",
    )
    data_hora__date__gte = django_filters.DateFilter(
        field_name="data_hora",
        lookup_expr="date__gte",
        label="Jogo a partir de",
        widget=date_input(),
    )
    data_hora__date__lte = django_filters.DateFilter(
        field_name="data_hora",
        lookup_expr="date__lte",
        label="Jogo até",
        widget=date_input(),
    )
    modalidade = django_filters.ModelChoiceFilter(
        queryset=Modalidade.objects.order_by("nome"), label="Modalidade"
    )
    etapa = django_filters.ModelChoiceFilter(
        queryset=Fase.objects.order_by("sequencia"), label="Fase"
    )
    resultado__icontains = django_filters.CharFilter(
        field_name="resultado", lookup_expr="icontains", label="Resultado contém"
    )

    class Meta:
        model = Jogo
        fields = {
            "time_1__nome_time": ["icontains"],
            "time_2__nome_time": ["icontains"],
            "data_hora": ["date__gte", "date__lte"],
            "modalidade": ["exact"],
            "etapa": ["exact"],
            "resultado": ["icontains"],
        }