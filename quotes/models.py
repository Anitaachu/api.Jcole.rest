from django.db import models


# Create your models here.


class Cole(models.Model):
    quote = models.CharField(max_length=1000)


    class Meta: 
        ordering = ['quote']

    def __str__(self):
        return self.quote





