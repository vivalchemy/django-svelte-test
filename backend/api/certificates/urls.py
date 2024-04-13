from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CertificatesViewSet

certificates_router  = DefaultRouter()
certificates_router.register('certificates', CertificatesViewSet)
