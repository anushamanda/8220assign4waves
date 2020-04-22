from django.urls import path, re_path
from .import views




urlpatterns=[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('forms', views.forms, name='forms'),
    path('uploadforms', views.uploadforms, name='uploadforms'),
    path('contact', views.contact, name='contact'),
    path('<int:form_id>', views.form, name='form'),
    path('search', views.search, name='search'),
    re_path(r'^home/$', views.home, name='home'),

]