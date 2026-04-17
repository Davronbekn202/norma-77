from django.contrib import admin
from django.urls import path,include
from firstapp.views import contact_view, success_view
from accounts.views import profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contact_view, name='contact'),
    path('success/', success_view, name='success'),
    path('account/',include('accounts.urls')),
    path('profile/', profile, name='profile'),
]