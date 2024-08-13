from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    book_capacity = models.IntegerField()
    current_bookings = models.IntegerField(default=0)

    def __str__(self):
        return self.name
