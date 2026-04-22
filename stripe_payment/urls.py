from django.contrib import admin
from django.urls import path, include
from payments import views as payment_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', payment_views.welcome, name='welcome'),
    path('payment/', include('payments.urls')),  # Include payments app URLs
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)