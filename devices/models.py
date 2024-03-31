from django.db import models
from datetime import datetime
# Create your models here.


class Device(models.Model):
    location = models.CharField(max_length=100)
    last_checkin = models.DateTimeField(null=True, blank=True)

    def heartbeat(self):
        self.last_checkin = datetime.utcnow()
        self.save()

