from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from beers.models import Beer, Company, EspecialIngredients
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views import View
from beers.forms import CompanyForm, BeerForm, BeerFormset
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from beers.mixins import AddMyBirthdayToContextMixin
from django.urls import reverse_lazy


# Create your views here.
"""
@login_required   #decorador para no permitir el acceso a esta view si no se está logeado
def beer_list_view(request):
    beer_list = Beer.objects.all()
    #print('counter', list_beer.count())   #cuenta el numero de cervezas totales

    #print('exist?', list_beer.filter(id=2))  #coge la cerveza con id=2

    #company = Company.objects.create(name='Heinekken Distri', tax_number = 1120)  #creamos una beer y una compañia
    #Beer.objects.create(name='Lager', company=company)
    
    #print(list_beer.filter(company__name__startswith="C", abv__gte = 4))  #AND

    #print(list_beer.filter( Q (company__name__startswith="C") | Q (abv__gte = 4))) #OR

    #Beer.objects.filter(pk = 4).first().delete  #delete

    #company = Company.objects.get(pk=1)  #las cervezas que como compañia tienen la cía pk = 1
    #print(company.beers.all()) 

    #company = Company.objects.get(pk=1)   #cambia el abv de todas las cervezas que tengan como compañia la pk=1
    #for beer in company.beers.all():
    #    beer.abv = 4.85
    #    beer.save()


    #special = EspecialIngredients(name='romero')    #creamos un ingrediente especial
    #special.save()

    #relacion manytomany
    #beer = Beer.objects.get(pk=3)  #se coge una cerveza para asignarle un ingrediente especial
    #ingredient = EspecialIngredients.objects.get(pk=1) #se coge el ingrediente especial a agregar
    #relacion
    #beer.especial_ingredients.add(ingredient)
    context = {
        'list_beer': beer_list
    }
    return render(request, 'beer_list.html', context)


#VIEWS EN FORMA DE CLASES CBV

#easy  - con menos funcionalidades y methods
class BeerListView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
        'beer_list': Beer.objects.all()
        }
        return render(request, 'beer_list.html', context)

#clase mas completa
class BeerListViewAlt(ListView):
    model = Beer

   def get_queryset(self):
        return Beer.objects.all()
        #return Beer.objects.filter(pk=2)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = context['beer_list'].first().company
        return context



#segunda vista - detail VIEW

@login_required
def beer_detail_view(request, pk):
    context = {
        'beer': Beer.objects.get(pk=pk)
    }
    return render(request, 'beer_detail.html', context)
"""


class BeerListView(ListView):
    model = Beer 


class BeerDetailView(DetailView):
    model = Beer
    
#con la clase formulario OLD
def company_edit_old(request, pk):

    company = get_object_or_404(Company, pk=pk)

    if request.method == 'POST':
        print('POST', request.POST)
        form = CompanyForm(request.POST)
        if form.is_valid():
            company.name = form.cleaned_data['name']
            company.tax_number = form.cleaned_data['tax_number']
            company.save()
    else:
        form = CompanyForm(initial={
            'name': company.name,
            'tax_number': company.tax_number
        })

    context = {
        'form': form
    }
    
    return render(request, 'company/company_form.html', context)

#con la clase CompanyFoms y una función
def company_edit(request, pk):

    company = get_object_or_404(Company, pk=pk)

    if request.method == 'POST':

        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():

            company.save()
            
    else:
        form = CompanyForm(instance=company)

    context = {
        'form': form
    }

    return render(request, 'company/company_form.html', context)

    
#clase que recoge el formulario
class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list-view')

class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list-view')

class CompanyDetailView(DetailView):
    model = Company

class CompanyListView(ListView):
    model = Company




class CompanyAndBeersCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = "beers/company_create_with_beers.html"
    success_url = reverse_lazy('company-list-view')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        if self.request.POST:
            ctx['beer_formset'] = BeerFormset(self.request.POST)
        else:
            ctx['beer_formset'] = BeerFormset()
        
        return ctx
    

    def form_valid(self, form):
        ctx = self.get_context_data()
        beer_formset = ctx['beer_formset']

        if beer_formset.is_valid():
            self.object = form.save()
            beer_formset.instance = self.object
            beer_formset.save()

        return super().form_valid(form)