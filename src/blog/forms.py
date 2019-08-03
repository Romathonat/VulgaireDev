from django import forms


class rechercheForm(forms.Form):
    recherche = forms.CharField(max_length=100)
