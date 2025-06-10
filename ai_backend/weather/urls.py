


from django.urls import path
from .views import weather_query

urlpatterns = [
    path('ask/', weather_query),
]
