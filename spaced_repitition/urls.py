from django.urls import path
from .views import CardListView, CardDetailView, CardCreateView, CardUpdateView, CardDeleteView, DeckCreateView
from . import views

urlpatterns = [
    path('', CardListView.as_view(), name='spaced_repitition-home'),
    path('home/', CardListView.as_view(), name='spaced_repitition-home'),
    path('card/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('card/<int:pk>/update', CardUpdateView.as_view(), name='card-update'),
    path('card/<int:pk>/delete', CardDeleteView.as_view(), name='card-delete'),
    path('card/new/', CardCreateView.as_view(), name='card-create'),
    path('deck/new/', DeckCreateView.as_view(), name='deck-create'),
    path('mypage/', views.mypage, name='spaced_repitition-mypage'),
    path('mypage/<int:pk>', views.mypage_study, name='spaced_repitition-mypage-study'), #Note, istedet for pk, vil jeg gerne have navntet på decket ind (men hvad gavner det?)

]
