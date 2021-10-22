from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.ImageField(upload_to = 'images/')
    def __str__(self):
        return self.title
