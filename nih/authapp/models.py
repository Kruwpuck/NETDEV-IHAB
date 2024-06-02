from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    showtime = models.DateTimeField()

    def __str__(self):
        return self.title

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.seat_number} - {self.movie.title}'
