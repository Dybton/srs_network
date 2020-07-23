from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Card, Deck, User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


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


class DeckCreateView(LoginRequiredMixin, CreateView):
    model = Deck
    fields = ['title']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('spaced_repitition-mypage')


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


@login_required(login_url="/login")
def mypage(request):
    current_user = request.user
    deck_title = 'History'  # This is where I need to get the deck I press
    context = {
        'decks': Deck.objects.filter(creator_id=current_user.id), 'cards': Card.objects.filter(decks__title=deck_title)
    }
    # context2 = {
    #     # Here I need to filter, so I only show our own decks
    #     # I need to get the id for the creator

    # }
    return render(request, 'spaced_repitition/mypage.html', context)

    # return render(request, 'content/details.html', {'content': content, 'reviews': Review.objects.filter(content_id=content_id)})


# @login_required(login_url="/login")
# def mypage_study(request):
#     current_user = request.user
#     deck_title = 'History'
#     context = {
#         'decks': Deck.objects.filter(creator_id=current_user.id), 'cards': Card.objects.filter(decks__title=deck_title)
#     }
#     # context2 = {
#     #     # Here I need to filter, so I only show our own decks
#     #     # I need to get the id for the creator

#     # }
#     return render(request, 'spaced_repitition/mypage.html', context)


# How can I pass the title of this deck into the deck title.
