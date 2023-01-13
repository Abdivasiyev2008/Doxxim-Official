from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class PaidPubgCheat(models.Model):
    name = models.CharField(max_length=100)
    about = RichTextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='paid-pubg-cheats/images/')
    video = models.FileField(upload_to='paid-pubg-cheats/videos/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']