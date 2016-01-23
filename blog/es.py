import elasticsearch
from elasticsearch_dsl import Search, Q
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from blog.models import Article


@receiver(post_delete, sender=Article)
def delete_article(instance, *args, **kwargs):
    es.delete(index='article', id=instance.id, doc_type='article', refresh=True)

@receiver(post_save, sender=Article)
def index_article(instance, *args, **kwargs):
    es.index(index='article', doc_type='article', id=instance.id, body={
        'titre': instance.titre,
        'auteur': instance.auteur.username,
        'contenu': instance.contenu,
        'preview': instance.preview,
        'publie': instance.publie
    })


def search_article(terms):
    q = (
        Q("match", titre=terms) | Q("match", contenu=terms) |
        Q("match", preview=terms) | Q("term", auteur=terms))

    response = Search(using=es, index='article').query(q).filter("term", publie=1).execute()
    results = []
    for hit in response.hits:
        results.append(Article.objects.get(id=hit.meta.id))
    return results

def regenerate_article_index():
    if es.indices.exists(index='article'):
        es.indices.delete(index='article')
    create_indexes()
    for article in Article.objects.all():
        index_article(article)

def create_indexes():
    if not es.indices.exists(index='article'):
        es.indices.create(index='article', body = {
            'settings':{
                'index':{
                    'analysis':{
                        'analyzer':{
                            'html_analyzer' :{
                                'type'     :    'custom',
                                'char_filter' : 'html_strip',
                                'tokenizer':    'standard',
                                'filter'   :    ['standard','lowercase', 'stop']
                            }
                        }
                    }
                }
            },
            'mappings':{
                'article':{
                    'properties':{
                        'titre':{
                            'type' : 'string'
                        },
                        'auteur' : {'type' : 'string'},
                        'contenu' : {
                            'type' : 'string',
                            'analyzer' : 'html_analyzer'
                        },
                        'preview' : {
                            'type' : 'string',
                            'analyzer' : 'html_analyzer'
                        },
                        'publie' : {'type' : 'boolean'}
                    }
                }
            }
        })



es = elasticsearch.Elasticsearch()
create_indexes()
