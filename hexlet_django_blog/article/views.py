from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# def index(request):
#     return render(request, 'articles/index.html')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "articles/index.html")
