from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Card
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


def home(request):
    context = {
        'cards': Card.objects.all()
    }
    return render(request, 'spaced_repitition/home.html', context)


class CardListView(ListView):
    model = Card
    template_name = 'spaced_repitition/home.html'
    context_object_name = 'cards'
    ordering = ['-date']


class CardDetailView(DetailView):
    model = Card


class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    fields = ['question', 'answer']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('spaced_repitition-home')


class CardUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Card
    fields = ['question', 'answer']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        card = self.get_object()
        if self.request.user == card.creator:
            return True
        return False

    def get_success_url(self):
        return reverse('spaced_repitition-home')


class CardDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # Note the mixins needs to be left of deleteview
    model = Card

    def test_func(self):
        card = self.get_object()
        if self.request.user == card.creator:
            return True
        return False

    def get_success_url(self):
        return reverse('spaced_repitition-home')


def mypage(request):
    return render(request, 'spaced_repitition/mypage.html')
