from django.urls import path
from .views import product_create,noproduct

urlpatterns = [
    path('', product_create, name='product_create'),
    path('creates/', noproduct, name='product_creates'),

]