from django.shortcuts import render

def index(request):
	return render(request, "base.html")

def search(request):
	search_result = request.GET.get("search")
	return render(request, "search.html", {"search": search_result})