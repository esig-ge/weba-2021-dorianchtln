# Dorian Châtelain
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect

# Create your views here.
from .forms import SalonForm
from .models import Parametres

#f
def gererSalon(request):
    return render(request, '../templates/gererSalon.html')

@staff_member_required
def modifier_salon(request, pk):
    if request.method == 'POST':
        pi = Parametres.objects.get(id=pk)
        fm = SalonForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('gererSalon')
    else:
        pi = Parametres.objects.get(id=pk)
        fm = SalonForm(instance=pi)
    return render(request, '../templates/modifier_salon.html', {'form': fm})

