# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Play_Project(models.Model):
    id = models.AutoField(primary_key=True)
    # This is a unique id that is set as a random string in views.py
    # {{
    unique_id = models.CharField(null=True, max_length=32, unique=True)
    # }}

    # This is a set of configurations
    # {{
    con_001 = models.CharField(max_length=16, null=True)
    # }}
    def __str__(self):
        return self.unique_id
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
