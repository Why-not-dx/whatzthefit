from django.shortcuts import render, redirect
from items.models import Item, Brand, Category
from .forms import SignUpForm, ContactForm
from items.forms import search_form
from django.db.models import Q
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
            messages.add_message(request, messages.SUCCESS, "Thanks for your message !")

            return redirect("/")
        else:
            messages.add_message(request, messages.SUCCESS, "Something went wrong, please try again.")

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
    items_with_user_posts = Item.objects.filter(item_posts__poster=request.user)
    
    return render(
        request,
        "core/account.html",
        {
            "items":user_items,
            "contribs":items_with_user_posts,
            "has_contribs": items_with_user_posts.exists(),
            "has_items": user_items.exists(),

        }
    )

def abouts(request):
    #/TODO create the contact form and check how to recieve messages -> create a model to have it in a data base and then sees them in the admin page
    # also need to add a post validation and a number a post per hour restriction for users to avoid botting
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            user_post = form.save(commit=False)
            user_post.user = request.user
            user_post.save()
            messages.add_message(request, messages.SUCCESS, "Thanks for your comment !")
            return redirect("/")

    else:
        form = ContactForm()
    
    return render(
        request,
        "core/abouts.html", {
            "form": form
        }
    )

def browse(request):
    query = request.GET.get('query', '')
    items = Item.objects.all().order_by("created_at")

    if request.method == "GET":
        form = search_form(request.GET)

        if form.is_valid():
            # form.save()
            cat_form = form.cleaned_data["category"] 
            brand_form = form.cleaned_data["brand"] 
            body_form = form.cleaned_data["body"] 
            if cat_form or brand_form or body_form:
                filters = Q()
                if cat_form:
                    filters &= Q(category=cat_form)
                if brand_form:
                    filters &= Q(brand=brand_form)
                if body_form:
                    filters &= Q(body=body_form)

                if filters:
                    items = items.filter(filters)
                
                return render(
                    request,
                    "core/browse.html",{
                        "items":items,
                        "query": query,
                        "form": form,}

    )

    else:
        form = search_form()
        

    if query:
        items = items.filter(Q(name__icontains=query) | Q(details__icontains=query))
    
    return render(
        request,
        "core/browse.html",{
            "items":items,
            "query": query,
            "form": form,}

    )
