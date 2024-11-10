from django.urls import path
from nanedu import views


urlpatterns = [
    path('', views.index, name='index'),
]