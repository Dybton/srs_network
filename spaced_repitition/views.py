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
    ordering = ['-date']

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
    card.decks.add(deck)
    card.save()
    deck.save()
    return redirect('/home/')

    # card = self.get_object()
    # deck = request.POST.get("deck_pk")
    # card.decks.add(deck)
    # print(card)

    # #request, deck_id (pk, I think), card_id,

    # return redirect('home')

    # def post(self, request, *args, **kwargs):
    #     name = request.POST.get("pk")
    #     product = Product.objects.get(pk=pk)

    # I need to use the update view I allready have and call it here.

    # Associate the Card with the new Publication:
    # card.decks.add(deck_3) I need to use this one.
    # I might need the get method here

    # def copy_card_to_deck(self, *args, **kwargs): #How do we call this function within our code?
    #     obj = Foo.objects.get(pk= < some_existing_pk > )  # Here we need to get the card object we are interested in
    #     obj.pk = None  # Then we set the pk to zero
    #     # Here we need to get the new deck and then save it to it.
    #     obj.save()  # We save the object, which genreates a new pk

    # Can I call the card create view, and then use that for creating a new card in the other deck?
    # Is it easier to create a new view?

    # Here we need to pass in the decks that the logged on user have access to

    # So here we need the deck titles, but we need to filter them based on the user.

    # def get_context_data(self, *args, **kwargs):
    #     deck = self.get_object()
    #     deck_title = deck.title
    #     context = super(DeckDetailView, self).get_context_data(*args, **kwargs)
    #     context['cards'] = Card.objects.filter(decks__title=deck_title)
    #     return context


class CardDetailView(DetailView):
    model = Card


class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    fields = ['question', 'answer']

    def form_valid(self, form):
        #card = self.get_object()
        form.instance.creator = self.request.user
        deck = get_object_or_404(Deck, pk=self.kwargs['deck_id'])
        card = self.get_object(Card)
        # self.card.decks.add(deck)
        #form.instance.decks = deck
        print(deck)
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


def remembered(request, pk, card_id):
    deck_id = pk
    card = get_object_or_404(Card, pk=card_id)
    card.days_till_study = card.days_till_study * 2
    card.save()
    return redirect('/mypage/' + str(deck_id))
