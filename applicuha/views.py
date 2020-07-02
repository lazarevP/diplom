from datetime import date

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView

from applicuha.forms import CustomUserCreationForm
from applicuha.models import CinemaUser, Seance


class Registration(CreateView):
    model = CinemaUser
    form_class = CustomUserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')


class Login(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('main_page')


def get(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect(reverse('main_page'))


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('main_page'))


class SeanceListView(ListView):
    model = Seance
    template_name = 'main_page.html'
    queryset = Seance.objects.all()
    paginate_by = 10

    def get_ordering(self):
        if self.request.GET.get('ordering'):
            return self.request.GET.get('ordering')

    def get_queryset(self):
        queryset = super().get_queryset()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context.update(
    #         {'search_form': OrderingForm, })
    #     return context


class TomorrowSeanceListView(ListView):
    model = Seance
    template_name = 'tomorrow.html'
    queryset = Seance.objects.all()
