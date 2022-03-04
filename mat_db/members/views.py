from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(response):
    if response.method == "POST":
        username = response.POST['username']
        password = response.POST['password']
        user = authenticate(response, username=username, password=password)
        if user is not None:
            login(response, user)
            return redirect("/")
        else:
            messages.success(response, ("The Was An Error Logging In, Try Again..."))
            return redirect("login")

    else:
        return render(response, "members/login.html", {})


def logout_user(response):
    logout(response)
    messages.success(response, ("You Were Succesfuly Loged Out"))
    return redirect("/")


