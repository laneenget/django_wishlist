from django.db import models

# Create your models here.

"""Describes a place table in the database, with a name and visited column.
Can add constraints, default values to the columns"""
class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}, visited? {self.visited}+'