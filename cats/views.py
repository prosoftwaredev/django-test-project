from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from cats.models import cats

class catsForm(ModelForm):
    class Meta:
        model = cats
        fields = ['name', 'date']

def home(request, template_name='cats/menu.html'):
    return render(request, template_name)

def cats_list(request, template_name='cats/cats_list.html'):
    cat = cats.objects.all()
    data = {}
    data['object_list'] = cat
    return render(request, template_name, data)

def cats_create(request, template_name='cats/cats_form.html'):
    form = catsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cats:cats_list')
    return render(request, template_name, {'form':form})

def cats_update(request, pk, template_name='cats/cats_form.html'):
    cat= get_object_or_404(cats, pk=pk)
    form = catsForm(request.POST or None, instance=cat)
    if form.is_valid():
        form.save()
        return redirect('cats:cats_list')
    return render(request, template_name, {'form':form})

def cats_delete(request, pk, template_name='cats/cats_confirm_delete.html'):
    cat= get_object_or_404(cats, pk=pk)
    if request.method=='POST':
        cat.delete()
        return redirect('cats:cats_list')
    return render(request, template_name, {'object':cats})
