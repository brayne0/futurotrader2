from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contacto/', views.contacto, name='contacto'),
    path('pagos/', views.pagos, name='pagos'),
    path('retiros/', views.retiros, name='retiros'),
    path('area-cliente/', views.area_cliente, name='area_cliente'),
]