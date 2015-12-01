from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    slug = models.SlugField(max_length=100)
    preview = RichTextUploadingField()
    contenu = RichTextUploadingField()
    publie = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de parution")

    categorie = models.ManyToManyField('Categorie')
    def __str__(self):
        return self.titre

@receiver(pre_save, sender=Article)
def testSlugAvantSave(sender, instance, *args, **kwargs):
    slugs = [article.slug for article in Article.objects.all() if article != instance]

    print(slugs)
    if instance.slug in slugs:
        print("entree2")
        instance.slug += "*"


class Categorie(models.Model):
    nom = models.CharField(max_length=30)
    couleur = models.CharField(max_length=30)
    def __str__(self):
        return self.nom