from django.db import models

from .author import Author
from .publisher import Publisher

class Series(models.Model):
    READ_DIRECTION_CHOICES = [
        ('D', 'Default'),
        ('L', 'Left'),
        ('R', 'Right'),
    ]

    title = models.CharField(default='None', max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default=1)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_DEFAULT, default=1)
    summary = models.TextField(default='None', max_length=500)

    read_direction = models.CharField(
        max_length=1,
        choices=READ_DIRECTION_CHOICES
    )

    def __str__(self):
        return self.title

    def get_read_direction(self):
        return read_direction
