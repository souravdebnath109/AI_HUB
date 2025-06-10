# currency/urls.py
from django.urls import path
from .views import analyze_pdf_view

urlpatterns = [
    path("analyze/", analyze_pdf_view, name="analyze_pdf"),
]

