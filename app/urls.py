from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('contractor_cabinet/', views.contractor_cabinet, name='customers'),
    path('customer_cabinet/', views.customer_cabinet, name='contractors'),
    path('contractor/<int:customer_id>', views.single_customer, name='single_customer'),
    path('customer/<int:customer_id>', views.single_contractor, name='single_contractor')
]
