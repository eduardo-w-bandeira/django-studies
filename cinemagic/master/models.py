from django.db import models

ROOM_CHOICES = [(num, f"Room {num}") for num in range(1, 6)]
SEAT_CHOICES = [(num, f"Seat {num}") for num in range(1, 101)]


class Movie(models.Model):
    title = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    genre = models.CharField(max_length=50)
    year = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'duration', 'year'], name='unique_movie')
        ]

    def __str__(self):
        return f"{self.title} ({self.year})"


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.IntegerField(choices=ROOM_CHOICES)
    showtime = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['room', 'showtime'], name='unique_showtime')
        ]

    def __str__(self):
        return f"{self.movie.title} at {self.showtime} in Room {self.room}"


class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    room = models.IntegerField(choices=ROOM_CHOICES)
    seat = models.IntegerField(choices=SEAT_CHOICES)
    booking_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['movie', 'room', 'showtime', 'seat'], name='unique_booking')
        ]

    def __str__(self):
        return f"Booking for {self.showtime.movie.title} by {self.customer_name}"
