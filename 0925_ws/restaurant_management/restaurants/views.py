from django.shortcuts import render, redirect
from .models import Restaurant

def index(request):
    restaurants = Restaurant.objects.all().order_by('id')
    return render(request, 'restaurants/index.html', {'restaurants': restaurants})

def new(request):
    return render(request, 'restaurants/new.html')

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        address = request.POST.get('address', '').strip()
        phone = request.POST.get('phone', '').strip()

        if name and address:  # 최소 유효성
            Restaurant.objects.create(
                name=name, description=description, address=address, phone=phone
            )
        return redirect('restaurants:index')
    return redirect('restaurants:new')
