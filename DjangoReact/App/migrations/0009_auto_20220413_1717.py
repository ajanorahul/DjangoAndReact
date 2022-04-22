# Generated by Django 2.2.5 on 2022-04-13 11:32

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_disc',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='disc',
            field=tinymce.models.HTMLField(),
        ),
    ]