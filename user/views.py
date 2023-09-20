from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
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
            return redirect('/')
    else:
        form = CustomUserCreationForm()
        print("No entro post")
    return render(request, './register.html', {'form': form,
                                               'msg': form.errors})