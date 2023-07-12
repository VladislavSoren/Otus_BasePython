from django.db import models


# Create your models here.

class ImageSexAgeDetect(models.Model):
    name = models.CharField(max_length=50)
    ImgSexAgeDetect = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
