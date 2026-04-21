from django.contrib import admin
from django.urls import path, include
from payments import views as payment_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', payment_views.welcome, name='welcome'),
    path('payment/', include('payments.urls')),  # Include payments app URLs
]