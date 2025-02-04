from .models import AttestModel
from django import forms

class AttestForm(forms.ModelForm):
    class Meta:
        model = AttestModel
        fields = ["ism", "familiya", "tell"]
        widgets = {
            "ism": forms.TextInput(attrs={"class": "form_control"}),
            "familiya": forms.TextInput(attrs={"class": "form-control"}),
            "tell": forms.TextInput(attrs= {"class": "form-control"})
        }

    

