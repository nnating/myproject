"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
# from storage import views as storageviews
#
# router = routers.DefaultRouter()
# router.register(r'user', storageviews.UserViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    url(r'^jwtutils-auth/', obtain_jwt_token),
    path('admin/', admin.site.urls),
    url(r'v1/', include('storage.urls')),
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('django_prometheus.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
