from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . models import Card
from django.urls import reverse
#from django.contrib.auth.mixins import LoginRequiredMixin

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


class CardCreateView(CreateView):
    model = Card
    fields = ['question', 'answer']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    # def get_absolute_url(self):
    #     return reverse('spaced_repitition-home', kwargs={'pk': self.pk})

    def get_success_url(self):
        return reverse('spaced_repitition-home')


def mypage(request):
    return render(request, 'spaced_repitition/mypage.html')
