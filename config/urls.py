from django.contrib import admin
from django.urls import path
from core.views import extract_csv_data

urlpatterns = [
    path("admin/", admin.site.urls),
    path("extract_csv_data/", extract_csv_data),  # API 엔드포인트
]