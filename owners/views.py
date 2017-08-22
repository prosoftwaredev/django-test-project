from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from owners.models import owners

class ownersForm(ModelForm):
    class Meta:
        model = owners
        fields = ['name', 'date']

@login_required
def owners_list(request, template_name='owners/owners_list.html'):
    if request.user.is_superuser:
        owner = owners.objects.all()
    else:
        owner = owners.objects.filter(user=request.user)
    data = {}
    data['object_list'] = owner
    return render(request, template_name, data)

@login_required
def owners_create(request, template_name='owners/owners_form.html'):
    form = ownersForm(request.POST or None)
    if form.is_valid():
        owners = form.save(commit=False)
        owners.user = request.user
        owners.save()
        return redirect('owners:owners_list')
    return render(request, template_name, {'form':form})

@login_required
def owners_update(request, pk, template_name='owners/owners_form.html'):
    if request.user.is_superuser:
        owner= get_object_or_404(owners, pk=pk)
    else:
        owner= get_object_or_404(owners, pk=pk, user=request.user)
    form = ownersForm(request.POST or None, instance=owner)
    if form.is_valid():
        form.save()
        return redirect('owners:owners_list')
    return render(request, template_name, {'form':form})

@login_required
def owners_delete(request, pk, template_name='owners/dogs_confirm_delete.html'):
    if request.user.is_superuser:
        owner= get_object_or_404(owners, pk=pk)
    else:
        owner= get_object_or_404(owners, pk=pk, user=request.user)
    if request.method=='POST':
        owner.delete()
        return redirect('owners:owners_list')
    return render(request, template_name, {'object':owners})
