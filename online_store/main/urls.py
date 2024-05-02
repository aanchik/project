from django.urls import path
from main import views 

urlpatterns: list = [
    path(' ', views.index, name='index'),
    path('about/', views.about, name='about'),
]