from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name="contact"),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]