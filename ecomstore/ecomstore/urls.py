from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls")),
]

handler404 = 'ecomstore.views.file_not_found_404'