from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home(request):
    services = Service.objects.all('-id')[:5]
    return render(request, 'main/home.html', {'services': services})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return redirect('/login')
    return render(request, 'main/register.html', {'form': form})

def services_view(request):
    services = Service.objects.all()
    return render(request, 'main/services.html', {'services': services})

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=id)
    return render(request, 'main/service_detail.html', {'service': service})

@login_required
def profile(request):
    return render(request, 'main/profile.html')

