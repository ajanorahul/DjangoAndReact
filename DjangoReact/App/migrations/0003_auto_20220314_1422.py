# Generated by Django 2.2.5 on 2022-03-14 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
