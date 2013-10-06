# bank/urls.py
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Account, Transaction
from .views import AccountList

urlpatterns = patterns('',
    url(r'^account/$',
        AccountList.as_view(),
        name='bank_account_list'),
    url(r'^account/create/$',
        CreateView.as_view(model=Account),
        name='bank_account_create'),
    url(r'^account/(?P<slug>[\w\-]+)/$',
        DetailView.as_view(model=Account),
        name='bank_account_detail'),
    url(r'^transaction/$',
        CreateView.as_view(model=Transaction,
                           success_url=reverse_lazy('bank_account_list')),
        name='bank_trans_create'),
)
