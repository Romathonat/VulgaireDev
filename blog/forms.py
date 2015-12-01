from django import forms
from captcha.fields import CaptchaField

class rechercheForm(forms.Form):
    recherche = forms.CharField(max_length=100)


class ContactForm(forms.Form):
    auteur = forms.EmailField(label="Votre adresse mail")
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()
