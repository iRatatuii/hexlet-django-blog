from django.urls import path
from django.views import View
from hexlet_django_blog.article.views import ArticleFormCreateView, IndexView, ArticleView

urlpatterns = [
    path("", IndexView.as_view(), name='articles'),
    path("<int:id>/", ArticleView.as_view(), name="article"),
    path('create/', ArticleFormCreateView.as_view(), name='article_create')
]
