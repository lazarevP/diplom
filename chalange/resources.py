from rest_framework import mixins, viewsets

from applicuha.models import CinemaUser, Hall, MovieInfo, Seance, Ticket
from chalange import serializers


class CinemaUserViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CinemaUser.objects.all()
    serializer_class = serializers.CinemaUserSerializer


class HallViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Hall.objects.all()
    serializer_class = serializers.HallSerializer


class MovieInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = MovieInfo.objects.all()
    serializer_class = serializers.MovieInfoSerializer


class SeanceViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Seance.objects.all()
    serializer_class = serializers.SeanceSerializer


class TicketViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
