from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils.timezone import now

from es import addArticle


# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.ForeignKey(User)
    slug = models.SlugField(max_length=100)
    preview = RichTextUploadingField()
    contenu = RichTextUploadingField()
    publie = models.BooleanField()
    date = models.DateTimeField(default=now() , verbose_name="Date de parution")

    categorie = models.ManyToManyField('Categorie')

    def __unicode__(self):
        return self.titre

    def __str__(self):
        return self.titre

    def save(self, * args, ** kwargs):
        ret = super(Article, self).save(* args, ** kwargs)
        addArticle(self)
        return ret



@receiver(pre_save, sender=Article)
def testSlugAvantSave(sender, instance, *args, **kwargs):
    slugs = [article.slug for article in Article.objects.all() if article != instance]

    if instance.slug in slugs:
        instance.slug += "*"


class ArticleProposition(models.Model):
    titre = models.CharField(max_length=100)
    contenu = RichTextUploadingField()
    categorie = models.ManyToManyField('Categorie')
    auteur = models.ForeignKey(User)

    def __unicode__(self):
        return self.titre

    def __string__(self):
        return self.titre


class Categorie(models.Model):
    nom = models.CharField(max_length=30)
    couleur = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nom

    def __str__(self):
        return self.nom


class Message(models.Model):
    auteur = models.ForeignKey(User)
    article = models.ForeignKey(Article)

    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de parution")
    publie = models.BooleanField()
    contenu = models.TextField()

    def __unicode__(self):
        return self.contenu

    def __str__(self):
        return self.contenu
