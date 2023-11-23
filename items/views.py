from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from .models import Item, Posts
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, new_post

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[0:3]

    fitgrade = Posts.objects.filter(item=item).aggregate(Avg("fit_grade", default=0))
    fitmeter = fitgrade['fit_grade__avg']

    if request.method == "POST":
        # Only 1 post per user and items
        form = new_post(request.POST)
        user_contrib_items = Posts.objects.filter(item=item, poster=request.user).exists()

        if form.is_valid() and not user_contrib_items :
            user_post = form.save(commit=False)
            user_post.item = item
            user_post.poster = request.user  # Assuming user is logged in maybe add a condition in HTML
            user_post.save()
            # Implement a pop up for the page when the form is checked and 
            # reload it with the new grade up.

    else:
        # Pass initial data to the form
        form = new_post(initial={'item': item.id}) 
        

    return render(
        request,
        "items/detail.html",
        {
            "item":item,
            "related_items":related_items,
            "new_form":form,
            "fitmeter": fitmeter
        }
    )

#TODO/ A user can only post 1 fit grade per item
#TODO/ we can't add an item that already exists : either make admin check forms before they go or create a filter
#TODO/ make it so a user can chose a brand OR create abrand by overriding a modelsForm widget class

@login_required
def new_item(request):
    form = NewItemForm()

    return render(request, "items/form.html", {
        "form": form,
        "title": "New item"
    })