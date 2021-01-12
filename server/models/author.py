from django.db import models

class Author(models.Model):
    first_name = models.CharField(default='None', max_length=25)
    last_name = models.CharField(default='None', max_length=25)
    middle_name = models.CharField(default='None', max_length=25)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['first_name', 'middle_name', 'last_name'],
                name='author_full_name'),
            models.CheckConstraint(
                check=models.Q(first_name is not None),
                name='author_check_if_first_name_exists')
        ]

    def __str__(self):
        return self.full_name()
