from django.db import models

# Create your models here.


class EntrepreneurUser(models.Model):
    # user_id = models.CharField(max_length=120) # max_length = required
    name = models.TextField(blank=True, null=True)
    surname = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    ideas = models.TextField(blank=True, null=True)
