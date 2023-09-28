from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from .forms import CustomUserCreationForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print("Entro post")
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print("Guardado")
            return redirect('/login/')
    else:
        form = CustomUserCreationForm()
        print("No entro post")
    return render(request, './register.html', {'form': form,
                                               'msg': form.errors})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm(),
                'msg': 'Usuario o contraseña invalidos'
            })
        else:
            print("Entro")
            auth_login(request, user)  # Aquí usamos el alias
            return redirect('/')
