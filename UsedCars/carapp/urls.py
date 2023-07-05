from django.urls import path
from . import views

app_name = 'carapp'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('allcars', views.allCars, name='allCars'),
    path('customer', views.customer_care, name='customer_care'),
    path('thank', views.thank, name='thank'),
    path('<slug:c_slug>/', views.allProdCat, name='cars_by_category'),
    path('<slug:c_slug>/<slug:car_slug>/', views.carDetail, name='carDetail'),
    path('<slug:c_slug>/<slug:car_slug>/booking/', views.booking, name='booking'),

]