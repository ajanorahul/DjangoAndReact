# Generated by Django 2.2.5 on 2022-03-25 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_disc', models.CharField(max_length=400)),
                ('long_disc', models.TextField()),
                ('image', models.ImageField(upload_to='image')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
