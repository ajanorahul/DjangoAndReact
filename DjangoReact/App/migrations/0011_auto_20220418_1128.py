# Generated by Django 2.2.5 on 2022-04-18 05:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_auto_20220413_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='long_disc',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='disc',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
