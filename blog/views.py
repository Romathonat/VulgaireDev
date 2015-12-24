# coding: utf-8
from django.shortcuts import render, get_list_or_404, get_object_or_404
from blog.models import Article, Categorie
from django.core.paginator import Paginator, EmptyPage
from blog.forms import rechercheForm
import re
from blog.forms import ContactForm, UtilisateurForm, ArticlePropositionForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db import IntegrityError

def home(request, page=1):
    articles = Article.objects.filter(publie=True).order_by("-date")
    paginationArticles = Paginator(articles, 8)

    try:
        articles = paginationArticles.page(page).object_list
    except EmptyPage:
        articles = paginationArticles.page(1).object_list

    return render(request, "accueil.html", locals())


def lire(request, slug):
    articles = get_list_or_404(Article, slug=slug, publie=True)  # si jamais plusieurs fois le même slug
    categories = [cat.nom for cat in articles[0].categorie.all()]
    tiret = "-"
    categories = tiret.join(categories)
    return render(request, 'lire.html', {'article': articles[0], 'categories': categories})


def categorie(request, nom):
    categorie = get_object_or_404(Categorie, nom=nom)
    articles = Article.objects.filter(categorie=categorie, publie=True)
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
                for motPreview in motsPreview:
                    if (motPreview == search):
                        appendIfUnique(resultatsRecherche, article)

    return render(request, 'recherche.html', locals())


def appendIfUnique(list, ajout):
    if ajout not in list:
        list.append(ajout)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            sujetValidate = form.cleaned_data['sujet']
            messageValidate = form.cleaned_data['message']
            auteurValidate = form.cleaned_data['auteur']

            send_mail(sujetValidate, messageValidate, auteurValidate, ['r.mathonat@laposte.net'], fail_silently=False)

            envoi = True
        else:
            data = request.POST
            sujet = data['sujet']
            message = data['message']
            auteur = data['auteur']
            error = True
    else:

        form = ContactForm()

    return render(request, 'contact.html', locals())


def registerUser(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)

        #on recupere les valeurs du formulaire pour les réafficher : si l'authentification est bonne, le formulaire ne s'affiche même pas
        username = request.POST['username']
        mail = request.POST['mail']

        if form.is_valid():
            if request.POST['password'] == request.POST['passwordConfirm']:
                try:
                    user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['mail'], form.cleaned_data['password'])
                    userCreated = True
                except IntegrityError:
                    userExist = True
            else:
                wrongPassword = True
        else:
            error = True

    else:
        form = UtilisateurForm()

    return render(request, 'registerUser.html', locals())


def proposeArticle(request):
    removeNav = True
    if request.method == 'POST':
        form = ArticlePropositionForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            data = request.POST
            sujet = data['sujet']
            message = data['message']
            auteur = data['auteur']
            error = True
    else:
        form = ArticlePropositionForm()
    return render(request, 'proposeArticle.html', locals())