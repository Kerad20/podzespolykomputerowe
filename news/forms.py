from django import forms
from news.models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model = Wiadomosci
        fields = ["image"]
