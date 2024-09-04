from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200, help_text="name of the movie")
    duration = models.FloatField(
        null=True, default=0.0, blank=True, help_text="in minutes"
    )
    rating = models.FloatField(
        null=True, default=0.0, blank=True, help_text="out of 10"
    )
    type = models.CharField(
        max_length=200, help_text="type of the movie", default="action"
    )
    image = models.ImageField(upload_to="images/", default="default.png")

    def __str__(self):
        return self.name
