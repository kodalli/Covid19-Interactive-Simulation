from django.db import models


class SimData(models.Model):
    healthyYoung = models.PositiveIntegerField(default=0)
    healthyYoungFreerider = models.PositiveIntegerField(default=0)
    sickYoung = models.PositiveIntegerField(default=0)

    healthyElderly = models.PositiveIntegerField(default=0) 
    healthyElderlyFreerider = models.PositiveIntegerField(default=0)
    sickElderly = models.PositiveIntegerField(default=0) 

    vaccines = models.PositiveIntegerField(default=0)

    timeSpan = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.healthyYoung)

    class Meta:
        ordering = []