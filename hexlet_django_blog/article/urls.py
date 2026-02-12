from django.urls import path
from django.views import View
from hexlet_django_blog.article.views import IndexView, ArticleView

urlpatterns = [
    path("", IndexView.as_view()),
    path("<int:id>/", ArticleView.as_view(), name="article"),
]
