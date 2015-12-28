from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.ForeignKey(User)
    slug = models.SlugField(max_length=100)
    preview = RichTextUploadingField()
    contenu = RichTextUploadingField()
    publie = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de parution")

    categorie = models.ManyToManyField('Categorie')
    def __str__(self):
        return self.titre

class ArticleProposition(models.Model):
    titre = models.CharField(max_length=100)
    contenu = RichTextUploadingField()
    categorie = models.ManyToManyField('Categorie')
    auteur = models.ForeignKey(User)

    def __str__(self):
        return self.titre


@receiver(pre_save, sender=Article)
def testSlugAvantSave(sender, instance, *args, **kwargs):
    slugs = [article.slug for article in Article.objects.all() if article != instance]

    if instance.slug in slugs:
        instance.slug += "*"


class Categorie(models.Model):
    nom = models.CharField(max_length=30)
    couleur = models.CharField(max_length=30)
    def __str__(self):
        return self.nom