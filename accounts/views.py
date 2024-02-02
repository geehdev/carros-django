from django.contrib.auth.forms import (
                                    UserCreationForm,
                                    AuthenticationForm,
                                    
                                        )
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

# Create your views here.
def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(
                    request,
                    template_name='register.html',
                    context={'user_form': user_form}
                    )


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # user retorna None se usúario não existir
        user = authenticate(
                                request, 
                                username=username,
                                password=password
                            )

        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()

    login_form = AuthenticationForm()         
    return render(
                    request, 
                    template_name='login.html',
                    context={'login_form': login_form}
                    )

def logout_view(request):
    logout(request)
    return redirect('cars_list')