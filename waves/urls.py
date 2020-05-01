from django.urls import path, re_path
from .import views





urlpatterns=[
    path('', views.landingpage, name='landingpage'),
    re_path(r'^home/$', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.index, name='events'),
    path('events/<int:event_id>', views.event, name='event'),
    #path('search', views.search, name='search'),
    path('enrollment/', views.enrollment, name='enrollment'),
    path('enrolled_events/', views.enrolled_events, name='enrolled_events'),
    path('enrolledevent_delete/<int:pk>/delete/', views.enrolledevent_delete, name='enrolledevent_delete'),
    path('enrollment_list/', views.enrollment_list, name='enrollment_list'),
    path('event/create/', views.event_new, name='event_new'),
    path('event/<int:pk>/update/', views.event_update, name='event_update'),
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),


]