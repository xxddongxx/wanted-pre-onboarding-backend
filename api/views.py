from rest_framework import viewsets

from api import serializers
from api.models import Company

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer


