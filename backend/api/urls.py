from rest_framework.routers import DefaultRouter
from api.certificates.urls import certificates_router
from django.urls import path, include

router = DefaultRouter()

router.registry.extend(certificates_router.registry)

urlpatterns = [
    path("", include(router.urls)),
]
