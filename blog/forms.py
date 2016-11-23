from django import forms
from captcha.fields import CaptchaField
from blog.models import *

class rechercheForm(forms.Form):
    recherche = forms.CharField(max_length=100)


class ContactForm(forms.Form):
    auteur = forms.EmailField(label="Votre adresse mail")
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()

class UtilisateurForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    mail = forms.EmailField(label="Votre adresse mail")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    captcha = CaptchaField()


class ArticlePropositionForm(forms.ModelForm):
    class Meta:
        model = ArticleProposition
        fields = ('titre','contenu','categorie')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('contenu',)
