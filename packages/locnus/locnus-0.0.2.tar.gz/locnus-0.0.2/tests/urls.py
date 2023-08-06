from django.urls import include, path

urlpatterns = [
    path("locnus/", include("locnus.urls", namespace="locnus")),
]
