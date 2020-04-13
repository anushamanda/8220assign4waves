from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views, forms as auth_forms
from django.urls import reverse_lazy
from django.contrib.auth import logout as django_logout

def register(request):
    if request.method=='POST':
       #get forms
       first_name= request.POST ['first_name']
       last_name=request.POST ['first_name']
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']

       #check password match
       if password==password2:
           #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'you are registered please login')
                    return redirect('login')
       else:
           messages.error(request, 'passwords do not match')
           return redirect('register')
    else:
        return render (request, 'accounts/register.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentails')
            return redirect('login')
    else:
        return render (request, 'accounts/login.html')

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
