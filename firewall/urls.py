# firewall/firewall/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Routing menuju app api
    path('api/', include('api.urls')),
]