from django.db import models

# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=25)
    designation=models.CharField(max_length=25)
    empid=models.IntegerField()

    def __str__(self):
        return self.name