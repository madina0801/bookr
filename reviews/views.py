from django.shortcuts import render
from django.http import HttpResponse 
from .models import Book

def welcome_view(request):
	message = f"<html><h1>Welcome to Bookr!</h1> <p>{Book.objects.count()} books and counting!</p></html>"
	return HttpResponse(message)

def index(request):
	return render(request, "base.html")

def search(request):
	search_result = request.GET.get("search")
	return render(request, "search.html", {"search": search_result})