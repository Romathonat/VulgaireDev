# coding: utf-8
import re

import requests
from requests.auth import HTTPBasicAuth
from misaka import Markdown, HtmlRenderer

from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator, EmptyPage

from blog.forms import rechercheForm
from blog.myViews.jumpSpecialView import jumpSpecialView
from blog.models import Article, Categorie


def home(request, page=1):
    articles = Article.objects.filter(publie=True).order_by("-date")
    pagination_articles = Paginator(articles, 8)

    try:
        page = int(page)
        articles = pagination_articles.page(page).object_list
    except EmptyPage:
        articles = pagination_articles.page(1).object_list

    return render(request, "accueil.html", locals())


def get_article_from_github(url_GitHub):
    url = (
            'https://raw.githubusercontent.com/Romathonat/vulgaireDevEntries/'
            'master/{}'.format(url_GitHub)
    )

    response = requests.get(
                url,
                auth=HTTPBasicAuth('Romathonat', '5$IX"{{xX}.6m"wk')
                )
    return response


def lire(request, slug):
    # on cherche l'article correspondant
    # si jamais plusieurs fois le même slug
    articles = get_list_or_404(Article, slug=slug, publie=True)
    article = articles[0]
    categories = [cat.nom for cat in article.categorie.all()]

    tiret = "-"
    categories = tiret.join(categories)
    contenu = ""
    envoi = False
    # si cet est article est special, on redirige vers la vue souhaitée : le
    # comportement est le même mais avec des trucs en plus

    url_GitHub = article.urlGitHub

    if url_GitHub != '':
        response = get_article_from_github(url_GitHub)

        if response.status_code < 300:
            rndr = HtmlRenderer()
            md = Markdown(rndr, extensions=('fenced-code', 'math'))
            article_markdown = md(response.content.decode('utf-8'))
        else:
            article_markdown = (
               'Error calling the GitHub API! Maybe there was too much '
               'requests today.'
            )

        retour = jumpSpecialView(request, locals())

        if retour:
            return retour

        return render(request, 'markdown.html', {
                        'article': article,
                        'categories': categories,
                        'contenu': contenu,
                        'envoi': envoi,
                        'article_markdown': article_markdown,
                        'url_github': url_GitHub
               })
    else:
        return render(request, 'lire.html',
                      {'article': article, 'categories': categories,
                       'contenu': contenu, 'envoi': envoi})


def categorie(request, nom):
    categorie = get_object_or_404(Categorie, nom=nom)
    articles = Article.objects.filter(
                    categorie=categorie,
                    publie=True
               ).order_by('-date')

    return render(request, 'categorie.html', locals())


def recherche(request):
    if request.method == "POST":
        form = rechercheForm(request.POST)
        if form.is_valid():

            search = form.cleaned_data['recherche']
            search = search.lower()

            articles = Article.objects.all()
            resultatsRecherche = []

            for article in articles:
                # les mots du contenu
                mots = re.sub(r'<.*?>|&nbsp;', ' ', article.contenu)
                mots = mots.split(" ")
                mots = [mot.lower() for mot in mots]
                for mot in mots:
                    if (mot == search):
                        appendIfUnique(resultatsRecherche, article)

                # les mots du titre
                motsTitre = article.titre.split(" ")
                motsTitre = [mot.lower() for mot in motsTitre]
                for motTitre in motsTitre:
                    if (motTitre == search):
                        appendIfUnique(resultatsRecherche, article)

                # les mots de la preview
                motsPreview = re.sub(r'<.*?>|&nbsp;', ' ', article.preview)
                motsPreview = motsPreview.split(" ")
                motsPreview = [mot.lower() for mot in motsPreview]
                for mot in motsPreview:
                    if (motsPreview == search):
                        appendIfUnique(resultatsRecherche, article)

    return render(request, 'recherche.html', locals())


def appendIfUnique(list, ajout):
    if ajout not in list:
        list.append(ajout)


def contact(request):
    return render(request, 'contact.html')
