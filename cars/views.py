from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Car
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CarModelForm
from django.views.generic import (ListView, 
                                  CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView,
                                  )
from datetime import datetime


# Create your views here.
class CarsListView(ListView):
    model = Car
    # current_year = datetime.now().year
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    
    
@method_decorator(decorator=login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars'
   

@method_decorator(decorator=login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    # success_url = '/cars/'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(decorator=login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
    