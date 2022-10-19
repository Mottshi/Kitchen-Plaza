from django.urls import path
from order import views


urlpatterns = [
    path('homepage/', views.homepage, name='homepage')
]