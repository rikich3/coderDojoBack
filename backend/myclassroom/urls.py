from django.urls import path
from . import views

urlpatterns = [
    path('clase/', views.clase, name='clase_backdoor'),
    path('clase/<int:miembro>', views.clase, name='clase'),
    path('', views.home, name='home'),
    path('loginUser', views.loginUser, name='login')
]

# app.com/clase/1 -> json() //docente
# app.com/clase/0 -> json() //estudiante
# app.com/clase/otros -> 