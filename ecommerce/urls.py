from django.urls import path
from ecommerce.views import base_view, category_view, product_view

urlpatterns = [
    path('category/<category_slug>', category_view, name='category_detail'),
	path('product/<product_slug>', product_view, name='product_detail'),
    path('', base_view, name='base'),
]
