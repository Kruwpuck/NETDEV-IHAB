from django.db import models
from django.utils import timezone
from datetime import timedelta

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default="Unknown")
    showtime = models.DateTimeField(default=timezone.now)
    release_year = models.IntegerField(default=timezone.now().year)
    duration = models.DurationField(default=timedelta(hours=0))
    poster_url = models.URLField(max_length=200, default='https://example.com/default-poster.jpg')

    def __str__(self):
        return self.title

    @property
    def seats(self):
        return list(self.seat_set.all())

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Seat {self.seat_number} for {self.movie.title}"

class Image(models.Model):
    caption = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img/%y")

    def __str__(self):
        return self.caption
