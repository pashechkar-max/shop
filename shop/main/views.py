from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
from .forms import RegisterForm, ServiceForm
from django.contrib.auth.decorators import login_required

def home(request):
    services = Service.objects.order_by('-id')[:5]
    return render(request, 'home.html', {'services': services})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'register.html', {'form': form})

def services_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service_detail.html', {'service': service})


@login_required
def service_add(request):
    if not request.user.is_staff:
        return redirect('home')

    form = ServiceForm(request.POST or None)
    if form.is_valid():
        service = form.save()
        return redirect('service_detail', service_id=service.id)
    return render(request, 'service_add.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')
