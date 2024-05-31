from django.db import models
from django.utils import timezone 
from datetime import timedelta # Import timezone for default value

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default="Unknown")
    showtime = models.DateTimeField(default=timezone.now)
    #poster = models.CharField(max_length=100)  # Path relatif ke file static
    release_year = models.IntegerField(default=timezone.now().year)
    duration= models.DurationField(default=timedelta(hours=0))
    poster_url = models.URLField(max_length=200, default='https://example.com/default-poster.jpg')  # Default URL for the poster image

    

    def _str_(self):
        return self.title

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    booked = models.BooleanField(default=False)

class Image(models.Model):
    caption=models.CharField(max_length=50)
    image=models.ImageField(upload_to="img/%y")
    
    def _str_(self):
        return self.caption