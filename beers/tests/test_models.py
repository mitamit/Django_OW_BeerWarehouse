from django.test import TestCase
from beers.models import Company, Beer

# Create your tests here.
class BasicTestClass(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        company = Company.objects.create(name="compaTest", tax_number=1)
        Beer.objects.create(name='be1Test', company=company)
        Beer.objects.create(name='be2Test', company=company)
        Beer.objects.create(name='be3Test', company=company)

    def test_is_alcoholic(self):
        beer = Beer.objects.get(pk=1)
        self.assertEquals(beer.is_alcoholic, True)

    def test_has_more_alcohol_than(self):
        beer = Beer.objects.get(pk=2)
        self.assertEquals(beer.has_more_alcohol_than(4), True)