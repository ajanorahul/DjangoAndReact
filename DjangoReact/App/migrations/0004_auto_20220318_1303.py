# Generated by Django 2.2.5 on 2022-03-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20220314_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]
