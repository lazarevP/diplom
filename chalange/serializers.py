from rest_framework import serializers

from applicuha.models import CinemaUser, Hall, MovieInfo, Seance, Ticket


class CinemaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaUser
        fields = ['id', 'username', 'wallet']


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ['hall_name', 'places', ]


class MovieInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieInfo
        fields = ['movie_name', 'movie_time', 'beginning_date', 'ending_date']


class SeanceSerializer(serializers.ModelSerializer):
    movie_info = MovieInfoSerializer()
    hall = HallSerializer()

    class Meta:
        model = Seance
        fields = ['movie_info', 'hall', 'price', 'begin_time', 'end_time']


class TicketSerializer(serializers.ModelSerializer):
    seance = SeanceSerializer()
    cinema_user = CinemaUserSerializer()

    class Meta:
        model = Ticket
        fields = ['seance', 'cinema_user']
