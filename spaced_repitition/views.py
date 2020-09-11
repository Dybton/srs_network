from django.shortcuts import render, get_object_or_404, redirect
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

    def get_queryset(self):
        return Card.objects.filter(copied=False)

    def get_context_data(self, *args, **kwargs):
        context = super(CardListView, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            context['decks'] = Deck.objects.filter(creator=self.request.user)
        return context


def copy_card(request, pk, card_id):
    deck_id = pk
    deck = get_object_or_404(Deck, pk=deck_id)
    card = get_object_or_404(Card, pk=card_id)
    card.pk = None
    card.save()
    card.days_till_study = 1
    card.copied = True
    card.deck = (deck)
    card.decks.add(deck)
    card.save()
    deck.save()
    return redirect('/home/')


class CardDetailView(DetailView):
    model = Card


class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    fields = ['question', 'answer']

    def form_valid(self, form):
        #card = self.get_object()
        form.instance.creator = self.request.user
        deck = get_object_or_404(Deck, pk=self.kwargs['deck_id'])
        form.save()
        # form.instance.decks.set(deck)
        form.instance.decks.add(deck)
        return super(CardCreateView, self).form_valid(form)
        # print("YO!")
        # So what I need to do, is to pass the deck Id to this
        # deck_id = self.request.Deck
        #deck_id = 2
        # self.assign_card(deck_id)

        # deck = get_object_or_404(Deck, slug=self.kwargs[deck_id])
        # form.instance.decks = deck
        # return super().form_valid(form)  # I need this

    def get_success_url(self):
        return reverse('spaced_repitition-mypage')

    # def form_valid(self, form):
    #     deck = get_object_or_404(Deck, pk=self.kwargs[deck_id])
    #     form.instance.decks = deck
    #     return super(CardCreateView, self).form_valid(form)

    # def assign_card(self, deck_id):
    #     self.card = self.get_object(Card)
    #     self.deck = get_object_or_404(Deck, pk=deck_id)
    #     self.card.decks.add(deck)
    #     self.card.save()

    #     self.deck = get_object_or_404(Deck, pk=deck_id)
    #     self.card.decks.add(deck)
    #     self.card.save()


# Note the below is just inspiration for how to make it work.

        # Hmm, I actually just need to send them back from where they came

        # card = get_object_or_404(Card)
        # deck = get_object_or_404(Deck, pk=deck_id)
        # card.decks.add(deck)
        # card.save()

    # def get_context_data(self, *args, **kwargs):
    #     deck = self.get_object()
    #     deck_title = deck.title
    #     context = super(DeckDetailView, self).get_context_data(*args, **kwargs)
    #     context['cards'] = Card.objects.filter(
    #         decks__title=deck_title).filter(days_till_study=1)
    #     # If card was correct => *2 and then it shouldn't show
    #     return context

    #     deck_id = pk
    #     deck = get_object_or_404(Deck, pk=deck_id)
    #     card = get_object_or_404(Card, pk=card_id)
    #     card.pk = None
    #     card.save()
    #     card.days_till_study = 1
    #     card.decks.add(deck)
    #     card.save()
    #     deck.save()
    #     return redirect('/home/')


class DeckCreateView(LoginRequiredMixin, CreateView):
    model = Deck
    fields = ['title', 'description']

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


class DeckListView(LoginRequiredMixin, ListView):
    model = Deck
    template_name = 'spaced_repitition/mypage.html'
    context_object_name = 'decks'
    ordering = ['-date']

    def get_queryset(self):
        return Deck.objects.filter(creator=self.request.user)


class DeckDetailView(LoginRequiredMixin, DetailView):
    model = Deck

    def get_context_data(self, *args, **kwargs):
        deck = self.get_object()
        deck_title = deck.title
        context = super(DeckDetailView, self).get_context_data(*args, **kwargs)
        context['cards'] = Card.objects.filter(
            decks__title=deck_title).filter(days_till_study=1)
        return context


# This is for studying decks from my page
def remembered(request, pk, card_id, value):
    deck_id = pk
    card = get_object_or_404(Card, pk=card_id)
    if value is 0:
        card.days_till_study = card.days_till_study * 2
        card.save()
        print(value)
    else:
        card.days_till_study = 2
        card.save()
    return redirect('/mypage/' + str(deck_id))

# This is from study all cards. I use this one, because I don't have the deck_id and don't need it


def remembered_from_study(request, card_id, value):
    card = get_object_or_404(Card, pk=card_id)
    if value is 0:
        card.days_till_study = card.days_till_study * 2
        card.save()
        print(value)
    else:
        card.days_till_study = 2
        card.save()
    return redirect('/study')


def study_daily_cards(request):
    cards = Card.objects.filter(
        decks__creator=request.user).filter(days_till_study=1)
    return render(request, 'spaced_repitition/study.html', {'cards': cards})

    # pk of card
