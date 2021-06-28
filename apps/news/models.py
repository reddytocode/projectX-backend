from django.db import models


class News(models.Model):
    # Todo: inherit
    guid = models.TextField()
    title = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=200, blank=False)
    content = models.TextField()
    author = models.CharField(max_length=100, blank=False)