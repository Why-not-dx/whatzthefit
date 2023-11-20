from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Posts
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, new_post

def detail(request, pk):
    item =get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[0:3]


    if request.method == "POST":
        form = new_post(request.POST)

        if form.is_valid():
            user_post = form.save(commit=False)
            user_post.item = item
            user_post.poster = request.user  # Assuming user is logged in
            user_post.save()
            # Redirect or perform actions after saving the form

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