from rest_framework.serializers import ModelSerializer
from ..models import Certificates

class CertificatesSerializer(ModelSerializer):
    class Meta:
        model = Certificates
        fields = '__all__'
