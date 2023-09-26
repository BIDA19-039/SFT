from django.urls import path
from . import views


urlpatterns=[
    path('', views.homepage, name="homepage"),
    path('dataprocessing/<str:pk>/', views.dataprocessing, name="dataprocessing"),
    path('datasummary/', views.datasummary, name="datasummary" ),

    path('create-customer/', views.createCustomer, name="create=Customer" ),

    path('update-customer/<str:pk>/', views.updateCustomer, name="update-Customer"),

    path('delete-customer/<str:pk>/', views.deleteCustomer, name="delete-Customer"),


]