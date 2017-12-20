from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.ForeignKey(User)
    slug = models.SlugField(max_length=100)
    preview = models.TextField()
    urlGitHub = models.CharField(default='', max_length=200,
                                 null=True, blank=True)
    publie = models.BooleanField()
    date = models.DateTimeField(default=now(), verbose_name="Date de parution")
    categorie = models.ManyToManyField('Categorie')

    def __unicode__(self):
        return self.titre

    def __str__(self):
        return self.titre


@receiver(pre_save, sender=Article)
def test_slug_before_save(sender, instance, *args, **kwargs):
    slugs = [
                article.slug for article
                in Article.objects.all()
                if article != instance
            ]

    if instance.slug in slugs:
        instance.slug += "*"


class Categorie(models.Model):
    nom = models.CharField(max_length=30)
    couleur = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nom

    def __str__(self):
        return self.nom
