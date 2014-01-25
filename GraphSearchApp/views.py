from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def login(request):
	if request.user.is_authenticated():
		redirect("/")
	return render(request,'login.html')

def main(request):
	if not request.user.is_authenticated():
		redirect("/login/")

	return render(request,'main.html')

