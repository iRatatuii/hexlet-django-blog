from django.urls import path
from hexlet_django_blog.article.views import (
    ArticleFormCreateView,
    IndexView,
    ArticleView,
    ArticleFormEditView,
    ArticleDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="articles"),
    path("<int:id>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("<int:id>/edit/", ArticleFormEditView.as_view(), name="edit_article"),
    path("<int:id>/", ArticleView.as_view(), name="article"),
    path("create/", ArticleFormCreateView.as_view(), name="article_create"),
]
