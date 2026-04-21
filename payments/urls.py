from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_checkout_session, name='pay'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('refund/<int:payment_id>/', views.refund_payment, name='refund'),
]