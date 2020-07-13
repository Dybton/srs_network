from django.urls import path
from .views import CardListView, CardDetailView, CardCreateView
from . import views

urlpatterns = [
    path('', CardListView.as_view(), name='spaced_repitition-home'),
    path('home/', CardListView.as_view(), name='spaced_repitition-home'),
    path('card/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('card/new/', CardCreateView.as_view(), name='card-create'),
    path('mypage/', views.mypage, name='spaced_repitition-mypage'),

]
