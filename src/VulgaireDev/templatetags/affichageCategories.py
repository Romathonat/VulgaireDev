from blog.models import Categorie
from django import template

register = template.Library()


@register.inclusion_tag('menuCategories.html')
def affichageCategories():
    categories = Categorie.objects.all()
    return {'categories': categories}
