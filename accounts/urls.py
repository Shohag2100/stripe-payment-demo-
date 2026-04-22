from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='accounts-register'),
    path('verify-otp/', views.verify_otp, name='accounts-verify-otp'),
    path('resend-otp/', views.resend_otp, name='accounts-resend-otp'),
    path('login/', views.login_view, name='accounts-login'),
    path('token-refresh/', views.token_refresh, name='accounts-token-refresh'),
    path('me/', views.me, name='accounts-me'),
]
