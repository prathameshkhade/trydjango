from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .forms import SignupForm

# Create your views here.

def signup_view(request):
    if request.method == "POST":
        print("in post method")
        form = SignupForm(request.POST)
        print(form.is_valid()) 
        if form.is_valid():
            form.save()
            print("New User is created!")
            return redirect("/login/")

    else:
        form = SignupForm()

    return render(request, "try/signup.html", {
        "form": form
    })

def login_view(request):
    pass

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        print("loged out successful.")
        return redirect("/")

