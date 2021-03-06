from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Bookmark(models.Model):
    author = models.ForeignKey(User, null=True)
    title = models.CharField(max_length=100, blank=True,null=True)
    url = models.URLField('url',unique=True)

    def __str__(self):
        return self.title