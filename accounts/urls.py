from django.urls import path

from . import views

urlpatterns=[
    path ('login', views.login, name='login'),
    path ('register', views.register, name='register'),
    path ('logout', views.logout, name='logout'),
    path ('dashboard', views.dashboard, name='dashboard'),
    path('reset_password/', views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password/done/', views.PasswordResetDoneView.as_view(), name='reset_password_done'),
    path('reset_confirmation/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(), name='reset_password_confirmation'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='reset_password_complete'),
    path('change_password/', views.ChangePasswordResetDoneView.as_view(), name='change_password'),
    path('change_password_done', views.ChangePasswordResetDoneSuccessView.as_view(), name='change_password_done'),

]