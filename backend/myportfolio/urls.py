from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import include
from django.urls import re_path as url

urlpatterns = [url("admin/", admin.site.urls), url(r"^", include("apps.base.urls"))]
