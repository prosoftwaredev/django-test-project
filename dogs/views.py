from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from dogs.models import dogs

class dogsList(ListView):
    model = dogs

class dogsCreate(CreateView):
    model = dogs
    fields = ['name', 'date']
    success_url = reverse_lazy('dogs:dogs_list')

class dogsUpdate(UpdateView):
    model = dogs
    fields = ['name', 'date']
    success_url = reverse_lazy('dogs:dogs_list')

class dogsDelete(DeleteView):
    model = dogs
    success_url = reverse_lazy('dogs:dogs_list')