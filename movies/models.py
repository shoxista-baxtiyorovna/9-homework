from django.db import models
from django.shortcuts import reverse


class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)

    def get_detail_url(self):
        return reverse('movies:movie_detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('movies:movie_delete', args=[self.pk])

    def get_update_url(self):
        return reverse('movies:movie_update', args=[self.pk])