from django.urls import path
from .views import youtube_qa_view

urlpatterns = [
    path("ask/", youtube_qa_view, name="youtube-qa"),
]
