from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def scroll_view(request):
    return render(request, "scroll.html")
