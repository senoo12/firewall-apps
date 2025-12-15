# firewall/firewall/urls.py
from django.contrib import admin
from django.urls import path, include
from api.api.templates_view import EntryPointView, AllowedView, BlockedView

urlpatterns = [
    path('', EntryPointView.as_view()),  # landing
    path('allowed/', AllowedView.as_view()),
    path('blocked/', BlockedView.as_view()),

    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),
]
