from django.shortcuts import render, redirect
from items.models import Item, Brand, Category, Posts
from .forms import SignUpForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required


def welcome(request):
    items = Item.objects.all().order_by("created_at")[0:6]
    brands = Brand.objects.all()
    categories = Category.objects.all()
    

    return render(request, "core/welcome.html", {
        "items":items,
        "brands": brands,
        "categories":categories,
    })


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            new_user = authenticate(
                username=form.cleaned_data["username"], 
                password=form.cleaned_data["password1"],
                )
            login(request, new_user)

            return redirect("/")

    else:
        form = SignUpForm()

    return render(request, "core/signup.html", {
        "form": form
    })



@login_required(redirect_field_name="/welcome/")
def logout_user(request):
    logout(request)

    return redirect("/")


@login_required(redirect_field_name="/welcome/")
def account(request):
    user_items = Item.objects.filter(created_by=request.user)
    user_contribs = Posts.objects.filter(poster=request.user)[0:3]

    return render(
        request,
        "core/account.html",
        {
            "items":user_items,
            "contribs":user_contribs,
            "has_contribs": user_contribs.exists(),
            "has_items": user_items.exists(),

        }
    )
