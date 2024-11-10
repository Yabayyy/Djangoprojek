from django.urls import path
from sapps import views

urlpatterns = [
    path('', views.costumer, name='costumer'),
]