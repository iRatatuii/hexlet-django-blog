from email.policy import default
from random import choices
from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Article


@require_http_methods(["GET", "POST"])
def index(request):
    articles = Article.objects.all()
    # BEGIN (write your solution here)
    if request.method == "GET":
        return render(request, "articles/index.html", context={"articles": articles})
    else:
        Article.objects.create(
            title=request.POST.get("title"), author=request.POST.get("author")
        )
        # END
        return render(request, "articles/index.html", context={"articles": articles})


@require_http_methods(["GET"])
def article_view(request, id):
    # BEGIN (write your solution here)
    article = Article.objects.get(id=id)
    # END
    return render(request, "articles/article.html", context={"article": article})
