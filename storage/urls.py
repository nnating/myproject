# @Time     :2021/10/28 15:16
# @Author   :dengyuting
# @File     :urls.py
from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from storage import views

def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('companyslist/', views.companyslist),
    path('userslist/', views.userslist),
    path('companys/<int:pk>', views.company_detail),
    path('login/', views.login),
    path('gallerieslist/', views.gallerieslist),
    path('upload/', views.upload),
    path('fileslist/', views.fileslist),
    path('index/', views.index),
    path('sentry-debug/', trigger_error),
    path('roleslist/', views.roleslist),
    path('roles/<int:pk>', views.role_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)