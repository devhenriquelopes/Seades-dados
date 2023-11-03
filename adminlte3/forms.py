from django import forms
from .models import Municipio
from .models import Cisternas

class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = "__all__"

class CisternasForm(forms.ModelForm):
    class Meta:
        model = Cisternas
        fields = "__all__"