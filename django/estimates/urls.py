from django.urls import path
from . import views

app_name = 'estimates'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]