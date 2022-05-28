from django.db import models

from place.models import Place, Tag

# Create your models here.
class Room(models.Model):

    class ROOM_TYPE(models.IntegerChoices):
        ETC = 0, 'etc'
        CLS = 1, 'Classroom'
        RES = 2, 'Restaurant'

    name = models.CharField(max_length=100, null=False)
    number = models.PositiveSmallIntegerField(null=True)
    type = models.PositiveSmallIntegerField(choices=ROOM_TYPE.choices, default=ROOM_TYPE.ETC)
    floor = models.PositiveSmallIntegerField(null=True)
    building = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='rooms')
    information = models.CharField(max_length=500, null=True)
    tags = models.ManyToManyField(Tag, related_name='tag_rooms')
    
    def __str__(self):
        return self.name