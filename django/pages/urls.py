from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.ServiceListView.as_view(), name='service_list'),
    path('service/<int:pk>', views.ServiceDetailView.as_view(), name='service_detail'),
    # path('services/', views.services, name='services'),
    # path('services/radar', views.services_radar, name='services_radar'),
    # path('services/water_retention', views.services_water_retention, name='services_water_retention'),
    # path('services/water_retention_design', views.services_water_retention_design, name='services_water_retention_design'),
    # path('services/water_level_meter', views.services_water_level_meter, name='services_water_level_meter'),
    # path('cases/', views.cases, name='cases'),
    path('instances/', views.InstanceListView.as_view(), name='instance_list'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact/', views.contact, name='contact'),
    # path('orders/', views.OrdersView.as_view(), name='orders'),
]