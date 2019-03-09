from django.urls import path
from ecommerce.views import base_view

urlpatterns = [
    path('', base_view, name='base'),
]