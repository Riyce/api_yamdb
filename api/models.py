from django.db import models


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Жанр',
        max_length=30,
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class Category(models.Model):
    name = models.CharField(
        verbose_name='Категория',
        max_length=50,
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class Title(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
    )
    year = models.IntegerField(
        verbose_name='Дата выпуска',
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True,
        blank=True,
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='titles',
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
