from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^article/(?P<slug>.+)$', 'blog.views.lire', {},'lire'),
    url(r'^categorie/(?P<nom>.+)$', 'blog.views.categorie'),
    url(r'^recherche$', 'blog.views.recherche'),
    url(r'^proposeArticle$', TemplateView.as_view(template_name='proposeArticle.html'), name='proposeArticle'),
    url(r'^contact$', 'blog.views.contact'),
    url('^(?P<page>.+)$', 'blog.views.home'),
    url('^$', 'blog.views.home'),
    )+ static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
