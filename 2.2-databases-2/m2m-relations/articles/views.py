from django.shortcuts import render

from .models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'

    articles_objects = Article.objects.prefetch_related('scopes').order_by(ordering)

    articles = []
    for article in articles_objects:
        article_item = {
            'title': article.title,
            'text': article.text,
            'image': article.image,
            'published_at': article.published_at,
        }
        scopes_objects = article.scopes.all().values_list(
            'scopes__scope__tag__tag',
            'scopes__scope__is_main'
        )
        # unique items hack...
        scopes_set = set(scopes_objects)
        scopes_list = list(scopes_set)

        scopes = []
        for scope in scopes_list:
            scope_item = {
                'tag': {'name': scope[0]},
                'is_main': scope[1],
            }
            scopes.append(scope_item)

        article_item['scopes'] = scopes
        articles.append(article_item)

    context = {
        'object_list': articles
    }
    return render(request, template, context)
