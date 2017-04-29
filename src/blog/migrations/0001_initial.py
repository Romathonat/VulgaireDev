# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import django.utils.timezone
from django.conf import settings
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('preview', ckeditor_uploader.fields.RichTextUploadingField()),
                ('contenu', ckeditor_uploader.fields.RichTextUploadingField()),
                ('urlGitHub', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('publie', models.BooleanField()),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 9, 16, 17, 10, 1, 779252, tzinfo=utc), verbose_name=b'Date de parution')),
                ('auteur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleProposition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=100)),
                ('contenu', ckeditor_uploader.fields.RichTextUploadingField()),
                ('auteur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=30)),
                ('couleur', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Date de parution')),
                ('publie', models.BooleanField()),
                ('contenu', models.TextField()),
                ('article', models.ForeignKey(to='blog.Article')),
                ('auteur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='articleproposition',
            name='categorie',
            field=models.ManyToManyField(to='blog.Categorie'),
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ManyToManyField(to='blog.Categorie'),
        ),
    ]
