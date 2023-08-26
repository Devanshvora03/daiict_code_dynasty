from django.db import models

# Create your models here.

class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
# class EventCreation(models.Model):
#     event_title = models.CharField(max_length=200)
#     event_desc = models.CharField(max_length=200)
#     event_date = models.CharField(max_length=200)
#     event_time = models.DateTimeField()
#     event_format = models.CharField(max_length=200)