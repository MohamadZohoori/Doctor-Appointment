from django.urls import path
from . import views

urlpatterns = [
    path('get-ticket/', views.get_ticket, name='get_ticket'),
]
