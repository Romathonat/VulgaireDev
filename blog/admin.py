# -*- coding: utf-8 -*-

from django.contrib import admin
from blog.models import Categorie, Article, ArticleProposition, Message
from django.shortcuts import render, get_list_or_404, redirect
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from blog.es import regenerate_article_index


# permet de créer de creer une vue qui créer un article : on herite de modelAdmin pour modifier
class ArticlePropositionAdmin(admin.ModelAdmin):
    review_template = 'admin/blog/article/'

    def get_urls(self):
        urls = super(ArticlePropositionAdmin, self).get_urls()
        my_urls = patterns('',
                           (r'change/(?P<id>.+)/validerArticle/$', self.admin_site.admin_view(self.validerArticle)),
                           (r'(?P<id>.+)/validerArticle/$', self.admin_site.admin_view(self.validerArticle)),
                           )
        return my_urls + urls

    def validerArticle(self, request, id):
        articleProposition = ArticleProposition.objects.get(pk=id)
        article = Article(titre=articleProposition.titre, contenu=articleProposition.contenu,
                          auteur=articleProposition.auteur, publie=False)
        article.save()

        # on ajoute les categories(maniere la plus simple de le faire que j'ai trouve)
        article.categorie.add(*articleProposition.categorie.all())
        article.publie = False

        return redirect(reverse('admin:index'))



class ArticleAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super(ArticleAdmin, self).get_urls()
        my_urls = patterns('',
                           (r'^regenerate_article_index/$', self.admin_site.admin_view(self.rege_article_index)),
                           )
        return my_urls + urls

    def rege_article_index(self, index):
        regenerate_article_index()
        print('test')
        return redirect(reverse('admin:index'))


admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleProposition, ArticlePropositionAdmin)
admin.site.register(Message)
