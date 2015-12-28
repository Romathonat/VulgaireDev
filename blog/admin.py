# -*- coding: utf-8 -*-

from django.contrib import admin
from blog.models import Categorie, Article, ArticleProposition
from django.shortcuts import render, get_list_or_404, redirect
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse

#permet de creer de creer une vue qui créer un article
class ArticlePropositionAdmin(admin.ModelAdmin):
    review_template = 'admin/blog/article/'

    def get_urls(self):
        urls = super(ArticlePropositionAdmin, self).get_urls()
        my_urls = patterns('',
                           (r'(?P<id>.+)/validerArticle/$', self.admin_site.admin_view(self.validerArticle)),
                           )
        return my_urls + urls

    def validerArticle(self, request, id):
        articleProposition = ArticleProposition.objects.get(pk=id)
        article = Article(titre=articleProposition.titre, contenu=articleProposition.contenu, auteur=articleProposition.auteur ,publie=False)
        article.save()

        #on ajoute les categories(maniere la plus simple de le faire que j'ai trouve)
        article.categorie.add(*articleProposition.categorie.all())
        article.publie = False
        return redirect(reverse('admin:index'))


admin.site.register(Categorie)
admin.site.register(Article)
admin.site.register(ArticleProposition, ArticlePropositionAdmin)
