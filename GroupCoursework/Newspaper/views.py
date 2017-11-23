from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world")


def article_list_placeholder(request): # Testing purposes only
	return render(request, 'Newspaper/article_list.html')