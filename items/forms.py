from django import forms
from .models import Item, Posts



INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "body", "brand", "category", "details", "image"]
        widgets = {
            "category": forms.Select(
                attrs={"class": INPUT_CLASSES}
            ),
            "name": forms.TextInput(
                attrs={"class": INPUT_CLASSES}
            ),
            "details": forms.Textarea(
                attrs={"class": INPUT_CLASSES}
            ),
            "brand": forms.Select(
                attrs={"class": INPUT_CLASSES}
            ),
            "body": forms.Select(
                attrs={"class": INPUT_CLASSES}
            ),
            "image": forms.FileInput(
                attrs={"class": INPUT_CLASSES}
            ),
        }


class new_post(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["fit_grade"]
        widgets = {
            "fit_grade": forms.NumberInput(
                attrs={"class": INPUT_CLASSES}
                )}
        