from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/radar', views.services_radar, name='services_radar'),
    path('services/water_retention', views.services_water_retention, name='services_water_retention'),
    path('cases/', views.cases, name='cases'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact/', views.contact, name='contact'),
    path('orders/', views.OrdersView.as_view(), name='orders'),
]