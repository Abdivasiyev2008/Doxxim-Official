from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class FreePubgCheat(models.Model):
    name = models.CharField(max_length=120)
    about = RichTextField()
    cheat = models.FileField(upload_to='free-cheats/cheats/')
    image = models.ImageField(upload_to='free-cheats/images/')
    video = models.FileField(upload_to='free-cheats/videos/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']