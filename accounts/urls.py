from django.urls import path
from .views import register, CustomLoginView, CustomLogoutView, dashboard, update_profile, ChangePasswordView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', update_profile, name='profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
]






