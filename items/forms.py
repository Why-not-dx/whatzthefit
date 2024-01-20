from django import forms
from .models import Item, Posts, Brand, Body, Category
from django.template.defaultfilters import filesizeformat
from django.utils.translation import gettext_lazy as _
from django.conf import settings

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class NewItemForm(forms.Form):


    body_choices = tuple(Body.objects.all().values_list())
    cat_choices = tuple(Category.objects.all().values_list())

    def image_auth(image):
            max_size = settings.MAX_UPLOAD_SIZE
            curr_size = image.size
            if image:
                if curr_size > max_size:
                    raise forms.ValidationError(_(f'Please keep image under {int(max_size/1024)} Ko. Current filesize {int(curr_size/1024)} Ko'))
            else:
                raise forms.ValidationError(_('File type is not supported'))
            return image
    
    def no_url_check(text):
        if "http://" in text or "https://" in text or "www." in text:
            raise forms.ValidationError("As a safety measure, we don't allow urls in the description. Please remove it and try again.")
        else:
            return text

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
        validators=[no_url_check],
        required=False,
        widget=forms.Textarea(attrs={"class": INPUT_CLASSES})
        )
    image = forms.ImageField(
        validators=[image_auth],
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
        return cleaned_data   


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