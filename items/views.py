from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Item, Posts, Brand
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, new_post
from django.contrib import messages


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[0:3]
    
    user_contrib_items = Posts.objects.filter(item=item, poster=request.user).first()

    if request.method == "POST":
        # Only 1 post per user and items
        if user_contrib_items:
            form = new_post(request.POST, instance=user_contrib_items)
        else:
            form = new_post(request.POST)
        
        if form.is_valid():
            user_post = form.save(commit=False)
            user_post.item = item
            user_post.poster = request.user  # Assuming user is logged in maybe add a condition in HTML
            user_post.save()
            messages.add_message(request, messages.SUCCESS, "Thanks for your help !")
            #TODO/ reload the page with updated grade ? 
            #TODO/ change submit button into edit button if already graded

        else:
            # form = new_post(initial={'item': item.id}) 
            messages.add_message(request, messages.ERROR, "Someting went wrong, please try again")
                
    else:
        if user_contrib_items:
            form = new_post(instance=user_contrib_items)

        else:
            form = new_post(initial={'item': item.id})
    fitgrade = Posts.objects.filter(item=item).aggregate(Avg("fit_grade", default=0))
    fitmeter = round(fitgrade['fit_grade__avg'], 1)
    #/TODO add a remove button to remove the users post if they confused products
    
    return render(
        request,
        "items/detail.html",
        {
            "item":item,
            "related_items":related_items,
            "new_form":form,
            "fitmeter": fitmeter,
            "contributed": user_contrib_items,
        }
    )

#TODO/ we can't add an item that already exists : either make admin check forms before they go or create a filter
#TODO/ make it so a user can chose a brand OR create abrand by overriding a modelsForm widget class

@login_required
def new_item(request):
    brands = Brand.objects.all()

    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            form_data = form.data
            brand_name = form_data['brand']
            new_brand_name = form_data["new_brand"]
            print("brand :", brand_name, "new brand name : ", new_brand_name)

            if brand_name.lower() == "other":
                print("other")
                
                brand, created = Brand.objects.get_or_create(name=new_brand_name)
                # Use get_or_create to get an existing brand or create a new one then create the item
                Item.objects.create(
                    name=cleaned_data['name'],
                    body_id=cleaned_data['body'],
                    category_id=cleaned_data['category'],
                    details=cleaned_data['details'],
                    image=cleaned_data['image'],
                    brand=brand,
                    )

            else:
                brand_instance = Brand.objects.get(name=cleaned_data['brand'])
                
                Item.objects.create(
                    name=cleaned_data['name'],
                    body_id=cleaned_data['body'],
                    category_id=cleaned_data['category'],
                    details=cleaned_data['details'],
                    image=cleaned_data['image'],
                    brand=brand_instance,
                    )

            

            
            
            

            return redirect("/")

    else:
        form = NewItemForm()

    return render(request, "items/form.html", {
        "form": form,
        "title": "New item",
        "brands": brands
    })