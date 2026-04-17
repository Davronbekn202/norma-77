from django.urls import path,include
from firstapp.views import contact_view, success_view

urlpatterns = [
    path('', contact_view, name='contact'),
    path('success/', success_view, name='success'),
    path('account/',include('accounts.urls')),
]