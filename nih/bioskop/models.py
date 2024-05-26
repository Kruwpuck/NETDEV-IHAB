from django.db import models
from django.utils import timezone  # Import timezone for default value

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default="Unknown")
    showtime = models.DateTimeField(default=timezone.now)
    poster = models.ImageField(upload_to="img/%y")
    #poster = models.CharField(max_length=100)  # Path relatif ke file static
    

    def __str__(self):
        return self.title

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    booked = models.BooleanField(default=False)

class Image(models.Model):
    caption=models.CharField(max_length=50)
    image=models.ImageField(upload_to="img/%y")
    
    def __str__(self):
        return self.caption