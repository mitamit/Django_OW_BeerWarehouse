from django.test import TestCase
from beers.models import Company
from django.contrib.auth.models import User
from django.urls import reverse
from model_mommy import mommy

class CompanyListViewTest(TestCase):

    def setUp(self):
        mommy.make(Company, _quantity=12)
        self.user = mommy.make(User)


    def test_view_url_exists(self):
        url = '/beers/company/list/'
        self.client.force_login(self.user)
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)


    def test_view_returns_all_entries(self):
        url = '/beers/company/list/'
        self.client.force_login(self.user)
        resp = self.client.get(url)
        assert resp.context['object_list'].count() ==  Company.objects.all().count()


    def test_template(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('company-list-view'))
        self.assertTemplateUsed(resp, 'beers/company_list.html')


    def test_login(self):
        #self.client.force_login(User.objects.first())
        resp = self.client.get(reverse('company-list-view'))
        self.assertEquals(resp.status_code, 302)