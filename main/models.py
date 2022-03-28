from django.db import models


class Genre(models.Model):
    slug = models.SlugField(max_length=55, primary_key=True)
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name


class Manga(models.Model):
    CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии')
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='books')
    status = models.CharField(choices=CHOICES, max_length=20)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title