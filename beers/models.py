from django.db import models
from beers.utils import image_upload_location
from core.models import CommonInfo 

# Create your models here.

class Company(CommonInfo):
    name = models.CharField('Name', max_length=50)
    tax_number = models.IntegerField('Tax number', unique=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Beer(CommonInfo):
    COLOR_YELLOW = 1
    COLOR_BLACK = 2
    COLOR_AMBER = 3
    COLOR_BROWN = 4
    
    COLOR_CHOICES = (
        (COLOR_YELLOW, 'yellow'),
        (COLOR_BLACK, 'black'),
        (COLOR_AMBER, 'amber'),
        (COLOR_BROWN, 'brown'),
    )

    name = models.CharField('Name', max_length=50)
    abv = models.DecimalField('Alcohol by volume', max_digits=5, decimal_places=2, default=0)
    is_filtered = models.BooleanField('Is filtered', default=False)
    color = models.PositiveIntegerField('Color', choices=COLOR_CHOICES, default=COLOR_YELLOW)
    image = models.ImageField('Image', blank=True, null=True, upload_to=image_upload_location)
    company = models.ForeignKey(Company, related_name="beers", blank=True, null=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'beer'
        verbose_name_plural = 'beers'
        ordering = ['name']
    
    def __str__(self):
        return self.name

    #las properties son propiedades que no se guardan en la bbdd y aqui funciona como funcion
    #no reciben parametros
    @property
    def is_alcoholic(self):
        return self.abv > 0
    
    #funcion que recibe parametros
    def has_more_alcohol_than(self, alcohol):
        return self.abv > alcohol

class EspecialIngredients(CommonInfo):
    name = models.CharField('Name', max_length=50)
    beers = models.ManyToManyField(Beer, blank=True, null=True, related_name='especial_ingredients')

    class Meta:
        verbose_name = 'Especial ingredient'
        verbose_name_plural = 'Especial ingredients'
        ordering = ['name']
    
    def __str__(self):
        return self.name

