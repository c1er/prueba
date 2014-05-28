from django.forms import ModelForm
from django import forms
from models import *
class NuevousuarioForm(ModelForm):
	class Meta:
		model=Nuevousuario

