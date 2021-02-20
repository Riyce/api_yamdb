from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from users.models import User

class Genre(models.Model):
    name = models.CharField(
        verbose_name='Жанр',
        max_length=20,
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        verbose_name='Категория',
        max_length=50,
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


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
        blank=True,
        null=True,
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



class Review(models.Model):
    
    title_id =  models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Пост',
        related_name='reviews',
        blank=True,
        null=True,

    )

    text = models.CharField(
        max_length=200,
        verbose_name='Текст отзыва',
    )     

    score = models.IntegerField(
        verbose_name='Рейтинг',
    )  

    pub_date = models.DateTimeField(
        auto_now_add = True,
        verbose_name='Дата отзыва',
    )         

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор поста (пользователь)',
        related_name='reviews',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Comments(models.Model):
    review_id = models.ForeignKey(
        Review,
        on_delete=models.SET_NULL,
        verbose_name='id поста',
        related_name='comments',
        blank=True,
        null=True,

    )

    text = models.CharField(
        max_length=200,
        verbose_name='Коментарий',
    )     


    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор поста (пользователь)',
        related_name='comments',
        blank=True,
        null=True,
    )

    pub_date = models.DateTimeField(
        auto_now_add = True,
        verbose_name='Дата комментария',
    )   

    def __str__(self):
        return self.name




