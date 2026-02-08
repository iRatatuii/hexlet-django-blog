from django.shortcuts import redirect, render

def index(request):
    return redirect("article", tags='Python', article_id=42)


def article(request, tags, article_id):
    return render(
        request, "articles/articles.html", {"tags": tags, "article_id": article_id}
    )
