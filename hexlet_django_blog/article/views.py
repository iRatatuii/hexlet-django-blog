from platform import architecture
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .forms import CommentArticleForm, ArticleForm
from .models import ArticleComment

from hexlet_django_blog.article.models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, "articles/index.html", context={"articles": articles})


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(request, "articles/show.html", context={"article": article})


class CommentArticleView(View):
    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST)
        if form.is_valid():
            comment = ArticleComment(
                content=form.cleaned_data["content"],
            )
            comment.save()


    def get(self, request, *args, **kwargs):
        form = CommentArticleForm()
        return render(request, 'comment.html', {'form': form})


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article add successfully')
            return redirect('articles')
        messages.error(request, "Article did not save")

        return render(request, "articles/create.html", {"form": form})


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/edit.html', {'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)        
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Article updated successfully')
            return redirect('articles')
        else:
            return render(
                request, "articles/edit.html", {"form": form, "article_id": article_id}
            )
