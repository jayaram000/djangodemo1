#form definition

from django import forms
from books.models import book



class Bookform(forms.ModelForm):
    class Meta:
        model=book
        fields="__all__"