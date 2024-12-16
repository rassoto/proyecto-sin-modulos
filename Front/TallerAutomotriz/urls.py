from django.contrib import admin
from django.urls import path
from Vehiculos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('eliminar/<str:vehiculo_id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('modificar/', views.modificar_vehiculo, name='modificar_vehiculo'),
    path('', views.obtener_datos, name='home'),
]