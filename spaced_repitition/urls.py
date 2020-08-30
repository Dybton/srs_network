from django.urls import path
from .views import CardListView, CardDetailView, CardCreateView, CardUpdateView, CardDeleteView, DeckCreateView, DeckListView, DeckDetailView
from . import views

urlpatterns = [
    path('', CardListView.as_view(), name='spaced_repitition-home'),
    path('home/', CardListView.as_view(), name='spaced_repitition-home'),
    path('home/copy_card/<int:pk>/<int:card_id>',
         views.copy_card, name='copy_card'),
    path('card/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('card/<int:pk>/update', CardUpdateView.as_view(), name='card-update'),
    path('card/<int:pk>/delete', CardDeleteView.as_view(), name='card-delete'),
    path('card/new/<int:deck_id>/', CardCreateView.as_view(), name='card-create'),
    # This is the new one.
    # path('card/new/<int:deck_id>/assign_to_deck',
    #      views.assign_to_deck, name='card-assign'),
    path('deck/new/', DeckCreateView.as_view(), name='deck-create'),
    path('mypage/', DeckListView.as_view(), name='spaced_repitition-mypage'),
    path('mypage/<int:pk>/', DeckDetailView.as_view(),
         name='mypage-study-deck'),
    path('mypage/<int:pk>/<int:card_id>/<int:value>', views.remembered,
         name='remembered'),
    path('study', views.study_daily_cards, name='study-daily-cards'),
    path('study/<int:card_id>/<int:value>', views.remembered_from_study,
         name='remembered-from-study'),

]
