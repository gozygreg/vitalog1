from django.urls import path
from . import views

app_name = 'waitlist'

urlpatterns = [
    path('join/', views.join_waitlist, name='join'),
    path('success/', views.waitlist_success, name='success'),
]
