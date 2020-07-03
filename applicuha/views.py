from datetime import date, timedelta

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView

from applicuha.forms import CustomUserCreationForm, TicketForm
from applicuha.models import CinemaUser, Seance, Ticket


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

    def get_ordering(self):
        if self.request.GET.get('ordering'):
            return self.request.GET.get('ordering')

    def get_queryset(self):
        queryset = Seance.objects.filter(movie_info__beginning_date__lte=date.today(),
                                         movie_info__ending_date__gte=date.today())
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {'ticket_form': TicketForm, })
        return context


class TomorrowSeanceListView(ListView):
    model = Seance
    template_name = 'tomorrow.html'
    queryset = Seance.objects.all()

    def get_ordering(self):
        if self.request.GET.get('ordering'):
            return self.request.GET.get('ordering')

    def get_queryset(self):
        queryset = Seance.objects.filter(movie_info__beginning_date__lte=date.today() + timedelta(days=1),
                                         movie_info__ending_date__gte=date.today() + timedelta(days=1))
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {'ticket_form': TicketForm, })
        return context


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm

    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        user = get_object_or_404(CinemaUser, pk=self.request.user.id)
        seance = get_object_or_404(Seance, pk=self.request.POST.get("seance_id"))
        user.wallet -= seance.price
        user.save()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.cinema_user = self.request.user
        seance = Seance.objects.get(id=self.request.POST.get("seance_id"))
        self.object.seance = seance
        self.object.save()


class TicketsListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'tickets.html'
    queryset = Ticket.objects.all()

    def get_queryset(self):
        queryset = Ticket.objects.filter(cinema_user=self.request.user)
        return queryset

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['money_spent'] = self.request.user.purchases
    #     return context

