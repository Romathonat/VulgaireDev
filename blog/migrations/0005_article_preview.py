# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151124_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='preview',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Previex Default'),
            preserve_default=False,
        ),
    ]
