from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views, forms as auth_forms
from django.urls import reverse_lazy
from django.contrib.auth import logout as django_logout
from .decorators import unauthenticated_user
from .models import Profile
from .forms import CustomerRegistrationForm, UserLoginForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from forms.views import home


def register(request):
    if request.method == 'POST':
        user_form = CustomerRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            Profile.objects.create(user=new_user, is_firefighter=True)
            return render(request,
                          'accounts/login.html',
                          {'new_user': new_user})
    else:
        user_form = CustomerRegistrationForm()
    return render(request,
                  'accounts/register.html',
                  {'user_form': user_form})

def register_supervisor(request):
    if request.method == 'POST':
        user_form = CustomerRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            Profile.objects.create(user=new_user, is_supervisor=True)
            # property = Property.objects.get(apt_no=user_form.cleaned_data['apt_no'])
            # Tenant.objects.create(user=new_user, apt_no=property, lease_start_date=user_form.cleaned_data['lease_start_date'], lease_end_date=user_form.cleaned_data['lease_end_date'])
            return render(request,
                          'accounts/login.html',
                          {'new_user': new_user})
    else:
        user_form = CustomerRegistrationForm()
    return render(request,
                  'accounts/register_supervisor.html',
                  {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.profile.is_firefighter or user.is_superuser:
                        return render(request, 'pages/index.html')
                    elif user.profile.is_supervisor or user.is_superuser:
                        #return HttpResponseRedirect(reverse('register_supervisor'))
                        return render(request, 'supervisor/supervisordash.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    django_logout(request)
    return redirect ('index')

def dashboard(request):
    return render (request, 'accounts/dashboard.html')

class PasswordContextMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title,
            **(self.extra_context or {})
        })
        return context


class PasswordResetView(auth_views.PasswordResetView):
    form_class = auth_forms.PasswordResetForm
    template_name = 'reset_password.html'
    email_template_name = 'reset_password_email.html'
    success_url = reverse_lazy('reset_password_done')

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    form_class = auth_forms.PasswordResetForm
    template_name = 'reset_password_done.html'
    #success_url = reverse_lazy('reset_password_done')

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    form_class = auth_forms.SetPasswordForm
    template_name = 'reset_password_confirm.html'
    success_url = reverse_lazy('reset_password_complete')

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    form_class = auth_forms.PasswordResetForm
    template_name = 'reset_password_complete.html'
    #success_url = reverse_lazy('login.html')

class ChangePasswordResetDoneView(auth_views.PasswordChangeView):
    form_class = auth_forms.PasswordChangeForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('change_password_done')

class ChangePasswordResetDoneSuccessView(auth_views.PasswordChangeView):
    form_class = auth_forms.PasswordChangeForm
    template_name = 'change_password_done.html'

