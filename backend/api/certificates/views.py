from rest_framework.viewsets import ModelViewSet
from ..models import Certificates, Users
from .serializers import CertificatesSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class CertificatesViewSet(ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        # for i in range(10):
        #     Users.objects.create(
        #         name="user" + str(i), email="user" + str(i) + "@gmail.com"
        #     )
        Users.objects.filter(id=1).update(name="Vivalchemy")
        for user in Users.objects.all():
            print(user);
        return super().create(request, *args, **kwargs)
