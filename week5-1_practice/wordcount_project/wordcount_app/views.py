from django.shortcuts import render
from wordcount_app import wordcount_python

# Create your views here.


def home(request):
    return render(request, "home.html")


def result(request):
    text = request.GET["fulltext"]
    count = wordcount_python(text)
    return render(request, "result.html")
