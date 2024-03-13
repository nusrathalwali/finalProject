from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    genre = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('genre',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.genre

    def get_url(self):
        return reverse('movieapp:movie_by_category', args=[self.slug])


class Movie(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField()
    image = models.ImageField()
    date = models.DateField()
    actors = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    youtube_link = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class UserMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    image = models.ImageField()
    date = models.DateField()
    actors = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    youtube_link = models.URLField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    def get_url(self):
        return reverse('movieapp:movieDetail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    movie = models.ForeignKey(UserMovie, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.movie.title
