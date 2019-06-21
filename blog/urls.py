from django.urls import path
from . import views
from blog import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contato', views.contact, name="contact")
]
