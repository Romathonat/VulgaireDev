# coding: utf-8
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from blog.models import *
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
import os
import re
from blog.forms import *
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from blog.myViews.jumpSpecialView import jumpSpecialView

from django.template.loader import get_template
from django.http import HttpResponse
from django.template import RequestContext
import VulgaireDev.settings

import requests
from requests.auth import HTTPBasicAuth
from misaka import Markdown, HtmlRenderer

def home(request, page=1):
    articles = Article.objects.filter(publie=True).order_by("-date")
    paginationArticles = Paginator(articles, 8)

    try:
        page = int(page)
        articles = paginationArticles.page(page).object_list
    except EmptyPage:
        articles = paginationArticles.page(1).object_list

    return render(request, "accueil.html", locals())

def get_article_from_github(url_GitHub):
    password_github = os.environ.get('GITHUB_PASSWORD')
    print(password_github)
    response = requests.get('https://raw.githubusercontent.com/Romathonat/vulgaireDevEntries/master/' + url_GitHub,
                 auth=HTTPBasicAuth('Romathonat', '5$IX"{{xX}.6m"wk'))
    return response

def lire(request, slug):
    # on cherche l'article correspondant
    articles = get_list_or_404(Article, slug=slug, publie=True)  # si jamais plusieurs fois le même slug
    article = articles[0]
    categories = [cat.nom for cat in article.categorie.all()]


    tiret = "-"
    categories = tiret.join(categories)
    contenu = ""
    envoi = False
    # si cet est article est special, on redirige vers la vue souhaitée : le comportement est le même mais avec des trucs en plus (genre d'héritage)

    retour = jumpSpecialView(request, locals())

    if retour:
        return retour

    url_GitHub = article.urlGitHub;

    if url_GitHub != '':
        response = get_article_from_github(url_GitHub)

        if response.status_code < 300:
            rndr = HtmlRenderer()
            md = Markdown(rndr, extensions=('fenced-code',))
            article_markdown = md(response.content.decode('utf-8'))
        else:
            article_markdown = "Error calling the GitHub API! Maybe there was too much requests today."

        return render(request, 'markdown.html',
                      {'article': article, 'categories': categories,
                       'contenu': contenu, 'envoi': envoi, 'article_markdown': article_markdown, 'url_github': url_GitHub})
    else:
        return render(request, 'lire.html',
                      {'article': article, 'categories': categories,
                       'contenu': contenu, 'envoi': envoi})


def categorie(request, nom):
    categorie = get_object_or_404(Categorie, nom=nom)
    articles = Article.objects.filter(categorie=categorie, publie=True).order_by('-date')
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


