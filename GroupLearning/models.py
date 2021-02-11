from django.db import models

# Create your models here.

class Name(models.Model):
    col1 = models.CharField(max_length=32)
    col2 = models.IntegerField()
    col3 = models.DateField()

    def __str__(self):
        return col1

    def __unicode__(self):
        return col1