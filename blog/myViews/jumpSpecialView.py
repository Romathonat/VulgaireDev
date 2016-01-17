# coding: utf-8
from blog.myViews.lesChiffres import lesChiffres

# un switch case pour rediriger vers la bonne vue:
# ceci est utile pour les vues ds articles personnalisés où il y a du code à éxécuter
def jumpSpecialView(request, kwargs):
    return {
        'Les Chiffres': lesChiffres(request, kwargs),
        'autreCas': "autrevue",
    }.get(kwargs['articles'][0].titre, 0)
