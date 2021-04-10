from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout

# Widok logowania usera
class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                redirect_url = request.GET.get('next', 'index')
                return redirect(redirect_url)
            else:
                return redirect('login')

# Widok do wylogowania usera
class LogOutView(View):

    def get(self, request):
        logout(request)
        return redirect('index')
# Widok do rejestarcji usera
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            u = User.objects.create(username=username)
            u.set_password(password)
            u.save()
            return redirect('login')
        else:
            return render(request, 'form.html', {'form': form})

