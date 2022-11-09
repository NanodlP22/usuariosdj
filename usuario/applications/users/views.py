from django.shortcuts import render
from django.core.mail import send_mail
#reverse_lazy Paquete que nos permite llamar un template por el name
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import (View, CreateView)
from django.views.generic.edit import (FormView)

from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm, VerificationForm

from .models import User
from .funtions import code_generator

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'
    
    def form_valid(self, form):
        
        codigo = code_generator()
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'],
            codregistro = codigo
        )
        #enviar el codigo generado al email del usuario
        asunto = 'Confirmación de email'
        mensaje = 'Código de verificación: ' + codigo
        email_remitente = 'marcelodelape@gmail.com'
        
        send_mail(asunto, mensaje, email_remitente, form.cleaned_data['email'], )
        
        return HttpResponseRedirect(reverse('users_app:verification'))
 
    
class Login(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy ('home_app:panel')
    
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request, user)
        
        return super(Login, self).form_valid(form)
  
    
class LogoutView(View):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'user_app:login'
            )
        )
        
        
class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy ('users_app:login')
    login_url = reverse_lazy('user_app:login')
    
    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username = usuario.username,
            password = form.cleaned_data['passwoed1']
        )
        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
        
        return super(UpdatePasswordView, self).form_valid(form)
    
    
class CodeVerificationView(FormView):
    template_name = 'users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:login')

    def form_valid(self, form):
        return super(CodeVerificationView, self).form_valid(form)