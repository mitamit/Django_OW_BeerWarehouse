from rest_framework import serializers
from beers.models import Beer, Company

class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beer
        fields = ('name', 'abv', 'color', 'is_filtered', 'company')
        
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'tax_number')

