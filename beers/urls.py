from django.urls import path, re_path
from beers.views import BeerListView, BeerDetailView, CompanyUpdateView, CompanyDetailView, CompanyListView, CompanyCreateView, CompanyAndBeersCreateView

urlpatterns = [
    re_path(r'^list/$', BeerListView.as_view(), name='beer-list-view'),
    re_path(r'^detail/(?P<pk>\d+)$', BeerDetailView.as_view(), name='beer-detail-view'),

    re_path(r'^company/create/$', CompanyCreateView.as_view(), name='company-create-view'),
    re_path(r'^company/create-with-beers/$', CompanyAndBeersCreateView.as_view(), name='company-and-beers-create-view'),
    re_path(r'^company/edit/(?P<pk>\d+)$', CompanyUpdateView.as_view(), name='company-edit-view'),
    re_path(r'^company/detail/(?P<pk>\d+)$', CompanyDetailView.as_view(), name='company-detail-view'),
    re_path(r'^company/list/$', CompanyListView.as_view(), name='company-list-view'),
]
 