from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
import MySQLdb
import threading
import time
import numpy as np
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as dj_login
from .forms import LoginForm

if "RDS_HOSTNAME" in os.environ:
	HOST = os.environ['RDS_HOSTNAME']
	USER = os.environ['RDS_USERNAME']
	PASSWORD = os.environ['RDS_PASSWORD']
else:
	HOST = "aa1399ny6mg81bf.cdbfvjdoiol8.us-east-2.rds.amazonaws.com"
	USER = "alegis277"
	PASSWORD = "a3c543bt8f"

@login_required
def index(request):
	return render(request, 'index.html')


def login(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				remember_me = form.cleaned_data['remember_me']
				user = authenticate(username=username, password=password)
				if user is not None:
					dj_login(request, user)
					if not remember_me:
						request.session.set_expiry(0)
					return redirect('/')
				else:
					return render(request, 'login.html', {'form': form, 'errors': True})
			else:
				return render(request, 'login.html', {'form': form, 'errors': True})
		else:
			return render(request, 'login.html', {'form': LoginForm()})