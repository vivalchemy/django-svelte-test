from django.db import models


# Create your models here.
class Certificates(models.Model):
    name = models.CharField(max_length=100)
    font_size = models.IntegerField()
    font_weight = models.IntegerField()
    font_family = models.CharField(max_length=100)
    text_position = models.FloatField()
    image = models.ImageField(upload_to="certificates", blank=True, null=True)

    def __str__(self):
        return self.title


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
