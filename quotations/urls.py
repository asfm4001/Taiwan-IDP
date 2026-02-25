from django.urls import path
from . import views

app_name = 'quotations'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('quotation/preview/<int:pk>/', views.QuotationPreviewView.as_view(), name='preview_quotation'),
    path('quotation/convert_to_order/<int:pk>', views.convert_quotation_to_order, name='convert_quotation_to_order'),
    path('quotation/clone_from_worktype/<int:pk>', views.clone_from_worktype, name='clone_from_worktype'),
    # path('pdf/<int:order_no>/', views.pdf, name='pdf'),
    # path('pdf1/', views.generate_pdf, name='pdf1')
]