from django.urls import path
from .views import register_view,home
from django.contrib.auth import views as auth_views
from .views import home
urlpatterns = [
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout')
]