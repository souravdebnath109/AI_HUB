

from django.urls import path
from .views import summarize_topic

urlpatterns = [
    path('ask/', summarize_topic),
]
