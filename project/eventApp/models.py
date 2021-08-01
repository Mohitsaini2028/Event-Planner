from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    data = models.CharField(max_length=500)
    time = models.TimeField()
    image = models.ImageField(upload_to="eventApp/images",default="")
    location = models.CharField(max_length=255)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.event_name + "  -  " + str(self.time)
