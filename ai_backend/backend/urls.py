from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/currency/', include('currency.urls')),#
    path('api/weather/', include('weather.urls')),#
    path('api/youtube/', include('youtube_qa.urls')),#
    path('api/research/', include('research.urls')),#
    path('api/pdf/', include('pdf_query.urls')),#
]
