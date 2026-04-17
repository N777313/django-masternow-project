from django.urls import path
from .views import dashboard, create_order

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', create_order, name='create_order'),
]
