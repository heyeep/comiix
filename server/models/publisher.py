from django.db import models

class Publisher(models.Model):
    title = models.CharField(default='None', max_length=100)

    def __str__(self):
        return self.title
