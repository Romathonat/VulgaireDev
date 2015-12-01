# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('titre', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=42)),
                ('contenu', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('couleur', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ForeignKey(to='blog.Categorie'),
        ),
    ]
