from django import forms
from django.contrib.auth.forms import UserCreationForm

from applicuha.models import CinemaUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CinemaUser
        fields = UserCreationForm.Meta.fields


# ORDER = (
#     ('price', 'By price'),
#     ('begin_time', 'By start time')
# )
#
#
# class OrderingForm(forms.Form):
#     order = forms.ChoiceField(choices=ORDER)
