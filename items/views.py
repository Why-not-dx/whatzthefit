from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Posts
from django.http import HttpResponse

def detail(request, pk):
    item =get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[0:3]

    if request.method == "POST" and "fit_value" in request.POST:
        pass
        


    return render(
        request,
        "items/detail.html",
        {
            "item":item,
            "related_items":related_items,

        }
    )
