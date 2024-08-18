from django.urls import path
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car
from django.urls import reverse_lazy


class test_view(request):
    return render(request, 'test_template.html')

class CarListView(ListView):
    model = Car
    template_name = 'cars_app/car_list.html'  # You can specify your own template

class CarDetailView(DetailView):
    model = Car
    template_name = 'cars_app/car_detail.html'  # You can specify your own template

class CarCreateView(CreateView):
    model = Car
    fields = ['model', 'brand', 'price', 'is_bought', 'buyer', 'buy_time']
    template_name = 'cars_app/car_form.html'  # You can specify your own template
    success_url = reverse_lazy('car_list')

class CarUpdateView(UpdateView):
    model = Car
    fields = ['model', 'brand', 'price', 'is_bought', 'buyer', 'buy_time']
    template_name = 'cars_app/car_form.html'  # You can specify your own template
    success_url = reverse_lazy('car_list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars_app/car_confirm_delete.html'  # You can specify your own template
    success_url = reverse_lazy('car_list')
