from django.urls import path
from .views import CardListView, CardDetailView, CardCreateView, CardUpdateView, CardDeleteView, DeckCreateView, DeckListView, DeckDetailView
from . import views

urlpatterns = [
    path('', CardListView.as_view(), name='spaced_repitition-home'),
    path('home/', CardListView.as_view(), name='spaced_repitition-home'),
    path('card/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('card/<int:pk>/update', CardUpdateView.as_view(), name='card-update'),
    path('card/<int:pk>/delete', CardDeleteView.as_view(), name='card-delete'),
    path('card/new/', CardCreateView.as_view(), name='card-create'),
    path('deck/new/', DeckCreateView.as_view(), name='deck-create'),
    path('mypage/', DeckListView.as_view(), name='spaced_repitition-mypage'),
    path('mypage/<int:pk>/', DeckDetailView.as_view(),
         name='mypage-study-deck')
    # path('mypage/', views.mypage, name='spaced_repitition-mypage'),
    # path('mypage/int:pk/', views.mypage_study_deck,
    #      name='spaced_repitition-mypage_study_deck'),
    # path('mypage/deck', views.mypage_study, name='spaced_repitition-mypage-study'), #Note, istedet for pk, vil jeg gerne have navntet på decket ind (men hvad gavner det? )
]
