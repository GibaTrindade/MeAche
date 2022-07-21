from django import forms
from .models import Lugar

class LugarForm(forms.ModelForm):
	class Meta:
		model = Lugar
		fields = ('nome', 'descricao')