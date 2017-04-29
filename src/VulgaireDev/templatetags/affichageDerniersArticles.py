from blog.models import Article
from django import template

register = template.Library()


@register.inclusion_tag('menuDerniersArticles.html')
def affichageDerniersArticles():
    derniers_articles = Article.objects.filter(publie=True).order_by('-date')[:5]
    return {'derniers_articles': derniers_articles}
