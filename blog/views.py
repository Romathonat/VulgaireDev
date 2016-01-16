# coding: utf-8
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from blog.models import *
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
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


def home(request, page=1):
    articles = Article.objects.filter(publie=True).order_by("-date")
    paginationArticles = Paginator(articles, 8)

    try:
        page = int(page)
        articles = paginationArticles.page(page).object_list
    except EmptyPage:
        articles = paginationArticles.page(1).object_list

    return render(request, "accueil.html", locals())


def lire(request, slug):
    # on cherche l'article correspondant
    articles = get_list_or_404(Article, slug=slug, publie=True)  # si jamais plusieurs fois le même slug
    categories = [cat.nom for cat in articles[0].categorie.all()]

    try:
        messages = articles[0].message_set.all()
    except:
        messages = []

    tiret = "-"
    categories = tiret.join(categories)
    contenu = ""
    envoi = False

    # on s'occupe du formulaire pour poster des messages
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            contenu = form.cleaned_data['contenu']

            # si user est authentifie, on envoie le message
            if (enregistrerMessage(request, articles, contenu)):
                envoi = True
            else:
                # sinon on redirige vers l'authentification
                # on sauvegarde en variables de session le contenu
                request.session['contenuMessage'] = contenu

                response = redirect('connexion')
                response['Location'] += '?next=' + reverse('lire', kwargs={'slug': slug})
                return response

        else:
            data = request.POST
            contenu = data['contenu']

    elif (request.session.get('contenuMessage') != None):
        if (enregistrerMessage(request, articles, request.session.get('contenuMessage'))):
            envoi = True
        del request.session['contenuMessage']
        form = ContactForm()
    else:
        form = ContactForm()

    # si cet est article est speciale, on redirige vers la vue souhaitée
    retour = jumpSpecialView(articles[0].titre, request, articles[0], categories)

    if retour:
        return retour

    return render(request, 'lire.html',
                  {'article': articles[0], 'categories': categories, 'messages': messages, 'form': form,
                   'contenu': contenu, 'envoi': envoi})


# permet d'enregistrer un message, en testant si user est authentifie
def enregistrerMessage(request, articles, contenu):
    if (request.user.is_authenticated()):
        try:
            message = Message(auteur=request.user, article=articles[0], publie=False, contenu=contenu)
            message.save()
            # on envoie un mail pour notifier qu'il y a un nouveau message

            # on envoi un mail pour avertir
            message = "Un nouveau message a été posté : http://vulgairedev.fr/admin/blog/message/"
            send_mail("Nouveau message", message, "VulgaireDev", ['r.mathonat@laposte.net'],
                      fail_silently=False)
        except IndexError:
            print("erreur ce slug ne coresspond à aucun article")
        return True
    else:
        return False


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

            messageValidate = messageValidate + " from " + auteurValidate

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

        # on recupere les valeurs du formulaire pour les réafficher : si l'authentification est bonne, le formulaire ne s'affiche même pas
        username = request.POST['username']
        mail = request.POST['mail']

        if form.is_valid():
            if request.POST['password'] == request.POST['passwordConfirm']:
                try:
                    user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['mail'],
                                                    form.cleaned_data['password'])
                    userCreated = True
                    login(request, authenticate(username=form.cleaned_data['username'],
                                                password=form.cleaned_data['password']))
                    return redirect(request.GET.get('next', ''))
                except IntegrityError:
                    userExist = True
            else:
                wrongPassword = True
        else:
            error = True
    else:
        form = UtilisateurForm()
    return render(request, 'registerUser.html', locals())


@login_required(login_url='connexion')
def proposeArticle(request):
    removeNav = True
    if request.method == 'POST':
        form = ArticlePropositionForm(request.POST)

        if form.is_valid():
            articleProposition = ArticleProposition(titre=form.cleaned_data['titre'],
                                                    contenu=form.cleaned_data['contenu'],
                                                    auteur=request.user)
            articleProposition.save()
            articleProposition.categorie.add(*form.cleaned_data['categorie'].all())

            # on envoi un mail pour avertir
            message = "Une nouvelle demande d'article a été postée : http://vulgairedev.fr/admin/blog/articleproposition/"
            send_mail("Nouvelle demande d'article", message, "VulgaireDev", ['r.mathonat@laposte.net'],
                      fail_silently=False)

            valide = True
    else:
        form = ArticlePropositionForm()
    return render(request, 'proposeArticle.html', locals())
