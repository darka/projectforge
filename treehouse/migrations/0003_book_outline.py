# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treehouse', '0002_book_abbreviation'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='outline',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
