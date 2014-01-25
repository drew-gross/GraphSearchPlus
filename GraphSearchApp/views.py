from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
	return render(request,'login.html')

def main(request):
	if request.user.is_authenticated():
		graph = request.user.get_offline_graph()
		print graph.get('me/photos/')
	return render(request,'main.html')
def index(request):
	return HttpResponse("Test");
