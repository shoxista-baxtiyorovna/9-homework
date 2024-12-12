from django.db import models
from django.shortcuts import reverse


class Travel(models.Model):
    destination_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    pop_season = models.CharField(max_length=100)

    def get_detail_url(self):
        return reverse('travels:travel_detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('travels:travel_delete', args=[self.pk])

    def get_update_url(self):
        return reverse('travels:travel_update', args=[self.pk])
