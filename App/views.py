from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
import MySQLdb
import threading
import time
import numpy as np
import os

if "RDS_HOSTNAME" in os.environ:
	HOST = os.environ['RDS_HOSTNAME']
	USER = os.environ['RDS_USERNAME']
	PASSWORD = os.environ['RDS_PASSWORD']
else:
	HOST = "aa1399ny6mg81bf.cdbfvjdoiol8.us-east-2.rds.amazonaws.com"
	USER = "alegis277"
	PASSWORD = "a3c543bt8f"

def index(request):
	return render(request, 'index.html')