from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from applicuha.models import CinemaUser, Ticket


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CinemaUser
        fields = UserCreationForm.Meta.fields


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = []
