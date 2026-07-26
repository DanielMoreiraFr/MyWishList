from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.view_entrada, name='entrada'),
    path('profile/', views.perfil_proprio, name='perfil_proprio'),
]
