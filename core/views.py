from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required


def index(request): 
    items = Item.objects.filter(is_sold=False)[0:9]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    form = SignupForm(request.POST or None) 

    if request.method == 'POST':  
        if form.is_valid():  
            form.save()
            return redirect('/login/')

    return render(request, 'core/signup.html', {'form': form})



@login_required
def user_logout(request):

    auth.logout(request)

    return redirect("/")



