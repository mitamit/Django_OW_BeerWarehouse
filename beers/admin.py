from django.contrib import admin
from beers.models import Beer, Company, EspecialIngredients
# Register your models here.

class BeerAdmin(admin.ModelAdmin):
    list_display = ('name', 'abv', 'is_filtered', 'color')
    list_filter = ('name', 'color',)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'tax_number')
    list_filter = ('name', 'tax_number',)

admin.site.register(Beer, BeerAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(EspecialIngredients) 