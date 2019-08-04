# coding: utf-8

import re
import os

import requests
from requests.auth import HTTPBasicAuth
from misaka import Markdown, HtmlRenderer

from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.conf import settings 

from nbconvert import HTMLExporter
from nbformat import reads as format_read

from blog.forms import rechercheForm
from blog.myViews.jumpSpecialView import jump_special_view
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


def get_article_from_github(url_article):
    '''
    url = (
            'https://raw.githubusercontent.com/Romathonat/vulgaireDevEntries/'
            'master/{}'.format(url_GitHub)
    )

    GITHUB_PASSWORD = os.environ.get("GITHUB_PASSWORD", '')

    response = requests.get(
                url,
                auth=HTTPBasicAuth('Romathonat', GITHUB_PASSWORD)
                )
    '''
    url = os.path.join('vulgaireDevEntries', url_article)
    url = os.path.join('static', url)

    try:
        with open(os.path.join(settings.BASE_DIR, url), 'r') as f:
            response = f.read()
    except:
        response = 'Error'
    
    return response


def read(request, slug):
    articles = get_list_or_404(Article, slug=slug, publie=True)
    article = articles[0]
    categories = [cat.nom for cat in article.categorie.all()]

    tiret = "-"
    categories = tiret.join(categories)

    # for some special posts, we use js code, so we use specific template
    retour = jump_special_view(request, locals())

    if retour:
        return retour
    
    url_article = '{}'.format(getattr(article, 'urlGitHub'))

    response = get_article_from_github(url_article)

    extension = url_article.split('.')[1]

    if response != 'Error':
        if extension == 'md':
            rndr = HtmlRenderer()
            md = Markdown(rndr, extensions=('fenced-code', 'math'))
            article_markdown = md(response)
            return render(request, 'markdown.html', {
                    'article': article,
                    'categories': categories,
                    'article_markdown': article_markdown,
                    'url_github': url_article 
            })

        elif extension == 'ipynb':
            notebook = format_read(response)
            html_explorer = HTMLExporter()
            html_explorer.template_file = 'basic'
            (body, _) = html_explorer.from_notebook_node(notebook)

            return render(request, 'lire_ipynb.html', {
                    'article': article,
                    'ipynb': body,
                    'categories': categories,
            })

    else:
        article_markdown = (
           'Error reading this article!'
        )
        return render(request, 'markdown.html', {
                    'article': article,
                    'categories': categories,
                    'article_markdown': article_markdown,
                    'url_github': url_article 
           })


def categorie(request, nom):
    categorie = get_object_or_404(Categorie, nom=nom)
    articles = Article.objects.filter(
                    categorie=categorie,
                    publie=True
               ).order_by('-date')

    return render(request, 'categorie.html', locals())


def search(request):
    if request.method == "POST":
        form = rechercheForm(request.POST)
        if form.is_valid():

            search = form.cleaned_data['recherche']
            search = search.lower()

            articles = Article.objects.all()
            resultatsRecherche = []

            for article in articles:
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
