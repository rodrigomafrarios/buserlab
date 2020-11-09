from django.db import models

# Create your models here.
class Register(models.Model):
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(editable=False,auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(null=True)
    objects = models.Manager()