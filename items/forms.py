from django import forms
from .models import Item, Posts, Brand, Body, Category


INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class NewItemForm(forms.Form):

    body_choices = tuple(Body.objects.all().values_list())
    cat_choices = tuple(Category.objects.all().values_list())

    name = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(attrs={"class": INPUT_CLASSES})
        )
    body = forms.ChoiceField(
        choices=body_choices, 
        widget=forms.Select(attrs={"class": INPUT_CLASSES})
        )
    brand = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={"class": INPUT_CLASSES, "id": "brand-input"})
        )
    category = forms.ChoiceField(
        choices= cat_choices, 
        widget=forms.Select(attrs={"class": INPUT_CLASSES})
        )
    details = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"class": INPUT_CLASSES})
        )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={"class": INPUT_CLASSES})
        )

    # Add any additional fields or customization as needed

    def clean(self):
        cleaned_data = super().clean()
        brand_name = cleaned_data.get('brand')

        # Check if the selected brand is "other"
        if brand_name.lower() == 'other':
            new_brand_name = cleaned_data.get('new_brand', '')

            # Set the value of the brand field to the entered new brand value
            cleaned_data['brand'] = new_brand_name

            # You can perform additional validation or actions here if needed

        return cleaned_data


# class NewItemForm(forms.ModelForm):

#     brand = forms.CharField(
#         max_length=100, 
#         required=True, 
#         widget=forms.TextInput(
#             attrs={"class": "w-full py-4 px-6 rounded-xl border", "id": "brand-input"}
#             ))

#     class Meta:
#         model = Item
#         fields = ["name", "body", "brand", "category", "details", "image"]
#         widgets = {
#             "category": forms.Select(
#                 attrs={"class": INPUT_CLASSES}
#             ),
#             "name": forms.TextInput(
#                 attrs={"class": INPUT_CLASSES}
#             ),
#             "details": forms.Textarea(
#                 attrs={"class": INPUT_CLASSES}
#             ),
#             "body": forms.Select(
#                 attrs={"class": INPUT_CLASSES}
#             ),
#             "image": forms.FileInput(
#                 attrs={"class": INPUT_CLASSES}
#             ),
#         }


class new_post(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["fit_grade"]
        widgets = {
            "fit_grade": forms.NumberInput(
                attrs={"class": INPUT_CLASSES}
                )}  
        

class search_form(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["body", "brand", "category"]
        widgets = {
            "category": forms.Select(
                attrs={"class": INPUT_CLASSES}
            ),
            "brand": forms.Select(
                attrs={"class": INPUT_CLASSES}
            ),
            "body": forms.Select(
                attrs={"class": INPUT_CLASSES}
            ),
        }
    def __init__(self, *args, **kwargs):
        super(search_form, self).__init__(*args, **kwargs)
        self.fields['category'].required = False
        self.fields['brand'].required = False
        self.fields['body'].required = False