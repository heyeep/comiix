from django.db import models

from .series import Series
from .author import Author
from .publisher import Publisher

class Issue(models.Model):
    READ_DIRECTION_CHOICES = [
        ('D', 'Default'),
        ('S', 'Series'),
        ('L', 'Left'),
        ('R', 'Right'),
    ]

    series = models.ForeignKey(Series, on_delete=models.SET_DEFAULT, default=1)
    title = models.CharField(default='None', max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default=1)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_DEFAULT, default=1)
    summary = models.TextField(default='None', max_length=500)

    page_count = models.IntegerField(default=0)
    year = models.IntegerField(default=1900)
    month = models.IntegerField(default=1)
    day = models.IntegerField(default=1)

    filename = models.CharField(default='None', max_length=250)
    upload = models.FileField(upload_to='uploads/')

    comixology_id = models.CharField(default='None', max_length=25)
    comicvine_id = models.CharField(default='None', max_length=25)

    read_direction = models.CharField(
        max_length=1,
        choices=READ_DIRECTION_CHOICES,
        default=[0][0]
    )

    def __str__(self):
        return self.title

    def is_comic(self):
        return self.comic

    def get_read_direction(self):
        return self.read_direction
