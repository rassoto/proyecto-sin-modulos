from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import requests
from django.contrib.auth import logout

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return render(request, 'myapp/register.html')
        
        try:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            login(request, user)
            return redirect('home')
        except Exception as e:
            messages.error(request, str(e))
            return render(request, 'myapp/register.html')
    
    return render(request, 'myapp/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'myapp/Login.html', {'error': 'Invalid username or password'})
    return render(request, 'myapp/Login.html')

def obtener_datos(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    url = 'http://localhost:3000/vehiculos'
    headers = {'Clave-De-Autenticacion': 'm+rD%=&wH@EbLpg--bU$xa!KHr/jnl'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        datos = response.json()
    else:
        datos = {}

    return render(request, 'myapp/index.html', {'datos': datos})

def agregar_vehiculo(request):
    if request.method == 'POST':
        url = 'http://localhost:3000/agregarVehiculos'
        headers = {'Clave-De-Autenticacion': 'm+rD%=&wH@EbLpg--bU$xa!KHr/jnl'}
        data = {
            'modelo': request.POST['modelo'],
            'marca': request.POST['marca'],
            'placa': request.POST['placa'],
            'year': request.POST['year'],
            'cliente': request.POST['cliente'],
            'estado': request.POST['estado'],
            'mecanico': request.POST['mecanico'],
            'servicios': request.POST['servicios']
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            messages.success(request, 'Vehículo agregado correctamente')
        else:
            messages.error(request, 'Error al agregar el vehículo')
        return redirect('home')

def eliminar_vehiculo(request, vehiculo_id):
    url = f'http://localhost:3000/vehiculos/{vehiculo_id}'
    headers = {'Clave-De-Autenticacion': 'm+rD%=&wH@EbLpg--bU$xa!KHr/jnl'}
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        messages.success(request, 'Vehículo eliminado correctamente')
    else:
        messages.error(request, 'Error al eliminar el vehículo')
    return redirect('home')

def modificar_vehiculo(request):
    if request.method == 'POST':
        vehiculo_id = request.POST['vehiculoId']
        url = f'http://localhost:3000/vehiculos/{vehiculo_id}'
        headers = {'Clave-De-Autenticacion': 'm+rD%=&wH@EbLpg--bU$xa!KHr/jnl'}
        data = {
            'modelo': request.POST['modelo'],
            'marca': request.POST['marca'],
            'placa': request.POST['placa'],
            'year': request.POST['year'],
            'cliente': request.POST['cliente'],
            'estado': request.POST['estado'],
            'mecanico': request.POST['mecanico'],
            'servicios': request.POST['servicios']
        }
        response = requests.put(url, headers=headers, json=data)
        if response.status_code == 200:
            messages.success(request, 'Vehículo modificado correctamente')
        else:
            messages.error(request, 'Error al modificar el vehículo')
        return redirect('home')
    
    from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')