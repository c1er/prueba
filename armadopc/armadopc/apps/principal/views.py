from django.shortcuts import render,render_to_response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
#from django.contrib.auth import login, authenticate,logout
from django.db.models import Q 
import datetime
import json
from forms import *
from models import *

# Create your views here.

def  inicio(request):
	return render_to_response("index.html",{},RequestContext(request))
def Armadopc(request):
	return render_to_response("index2.html",{},RequestContext(request))

def logeo(request):
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if(form.is_valid):
			password=request.POST["password"]
			username=request.POST["username"]
			user=authenticate(username=username,password=password)
			if user:
				login(request,user)
				return HttpResponseRedirect("/auth/bienvenido")
			else:
				return render_to_response("principal/error.html",{},RequestContext(request))
	form=AuthenticationForm()
	return render_to_response("principal/logeo.html",{"form":form},RequestContext(request))
def cerrar(request):
	logout(request)

def registro_cliente(request):
	if request.method=='POST':
		form=NuevousuarioForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/clientes/')
	else:
		form=NuevousuarioForm()
	return render_to_response("registro_cliente.html",{'formulario':form},context_instance=RequestContext(request))


def clientes(request):
	clientes=Nuevousuario.objects.all()
	return render_to_response("clientes.html",{'clientes':clientes},context_instance=RequestContext(request))



