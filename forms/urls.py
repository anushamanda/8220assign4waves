from django.urls import path
from .import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('forms', views.forms, name='forms'),
    path('contact', views.contact, name='contact'),
    path('<int:form_id>', views.form, name='form'),
    path('search', views.search, name='search'),

]