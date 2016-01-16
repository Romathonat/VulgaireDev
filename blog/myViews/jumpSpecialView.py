from blog.myViews.lesChiffres import lesChiffres
from blog.views import *


# un switch case pour rediriger vers la bonne vue:
#ceci est utile pour les vues ds articles personnalisés où il y a du code à éxécuter
def jumpSpecialView(titre, request, article, categories):
    from blog.views import home
    return {
        'lesChiffres': lesChiffres(request),
        'autreCas': "autrevue",
    }.get(titre, 0)
