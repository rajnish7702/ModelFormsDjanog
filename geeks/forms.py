from django import forms
from .models import GeeksModel

class GeeksForms(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = "__all__"