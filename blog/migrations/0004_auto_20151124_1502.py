# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publie',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='contenu',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=True),
            preserve_default=False,
        ),
    ]
