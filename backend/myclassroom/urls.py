from django.urls import path
from . import views

urlpatterns = [
    path('clase/', views.clase, name='clase_backdoor'),
    path('clase/<int:miembro>', views.clase, name='clase'),
    path('', views.home, name='home'),
    path('loginUser', views.loginUser, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('createuser', views.create_appuser, name='createuser'),
    path('get_user_data/', views.get_user_data, name='get_user_data'),
]

# app.com/clase/1 -> json() //docente
# app.com/clase/0 -> json() //estudiante
# app.com/clase/otros -> 