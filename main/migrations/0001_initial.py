# Generated by Django 4.0.3 on 2022-03-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('slug', models.SlugField(max_length=55, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=55, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='mangas')),
                ('status', models.CharField(choices=[('in stock', 'В наличии'), ('out of stock', 'Нет в наличии')], max_length=20)),
                ('genre', models.ManyToManyField(to='main.genre')),
            ],
        ),
    ]
