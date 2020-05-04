from rest_framework import viewsets
from beers.api.serializers import BeerSerializer, CompanySerializer
from beers.models import Beer, Company



class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

