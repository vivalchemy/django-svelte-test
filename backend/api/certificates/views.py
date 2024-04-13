from rest_framework.viewsets import ModelViewSet
from ..models import Certificates
from .serializers import CertificatesSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class CertificatesViewSet(ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer
    parser_classes = (MultiPartParser, FormParser)
