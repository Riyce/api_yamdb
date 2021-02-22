from django.db import models

from users.models import User


class Genre(models.Model):
    name = models.CharField(verbose_name='Genre', max_length=30, )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['-id']


class Category(models.Model):
    name = models.CharField(verbose_name='Category', max_length=50, )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['-id']


class Title(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200, )
    year = models.IntegerField(verbose_name='Release date')
    category = models.ForeignKey(
        Category,
        verbose_name='Category',
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True,
        blank=True,
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Genre',
        related_name='titles',
    )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Title',
        related_name='reviews',
        blank=True,
        null=True,
    )
    text = models.CharField(max_length=200, verbose_name='Text', )
    score = models.IntegerField(verbose_name='Rating', )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Publication date',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Author',
        related_name='reviews',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.text[:20]

    class Meta:
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review',
            )
        ]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.SET_NULL,
        verbose_name='Review',
        related_name='comments',
        blank=True,
        null=True,
    )
    text = models.CharField(
        max_length=200,
        verbose_name='Text',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Author',
        related_name='comments',
        blank=True,
        null=True,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Publication date',
    )

    def __str__(self):
        return self.text[:20]

    class Meta:
        ordering = ['-pub_date']
