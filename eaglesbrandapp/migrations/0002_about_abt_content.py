# Generated by Django 3.2.5 on 2021-07-31 16:06

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('eaglesbrandapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='abt_content',
            field=tinymce.models.HTMLField(default='content', verbose_name='Content'),
            preserve_default=False,
        ),
    ]
