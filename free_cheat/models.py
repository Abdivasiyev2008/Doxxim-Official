from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
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

class CommentBlog(models.Model):
    blogpost_connected = models.ForeignKey(FreePubgCheat, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.blogpost_connected} - {self.author}"