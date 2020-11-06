from django.db import models

# Create your models here.
class Register(models.Model):
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=300)
    datetime = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.title