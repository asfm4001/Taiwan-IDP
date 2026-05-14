from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.services, name='services'),
    path('service/<slug:slug>/', views.service_detail, name='service_detail'),
    path('instances/', views.InstanceListView.as_view(), name='instance_list'),
    path('contact/', views.contact, name='contact'),
    # path('orders/', views.OrdersView.as_view(), name='orders'),
]