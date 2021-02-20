from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('redoc/', TemplateView.
         as_view(template_name='redoc.html'), name='redoc'),
    path('api/v1/', include('api.urls')),
    path('api/v1/auth/', include('users.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
