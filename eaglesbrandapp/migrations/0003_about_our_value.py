# Generated by Django 3.2.5 on 2021-07-31 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eaglesbrandapp', '0002_about_abt_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='our_value',
            field=models.TextField(blank=True, null=True, verbose_name='Our Values'),
        ),
    ]