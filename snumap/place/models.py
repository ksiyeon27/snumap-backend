from django.db import models

class Location(models.Model):
    latitude = models.FloatField(null=False) 
    longitude = models.FloatField(null=False)

class Tag(models.Model):
    name = models.CharField(max_length=30, null = False)

# Create your models here.
class Place(models.Model):

    # https://docs.djangoproject.com/en/3.0/ref/models/fields/#enumeration-types
    class PLACE_CATEGORY(models.TextChoices):
        ETC = 0, '시설(etc)'
        HUM = 1, '인문대학'
        EDU = 2, '사범대학'
        CSS = 3, '사회과학대학'
        SCI = 4, '자연과학대학'
        PHA = 5, '약학대학'
        ENG = 6, '공과대학'
        ART = 7, '미술대학 및 음악대학'
        CBA = 8, '경영대학'
        VET = 9, '수의과대학'
        CHE = 10, '생활과학대학'
        CAL = 11, '농업생명과학대학'
        CLS = 12, '자유전공학부'
        ADM = 13, '행정대학원'
        ENV = 14, '환경대학원'
        INT = 15, '국제대학원'
        DEN = 16, '치의학대학원'
        LAW = 17, '법학전문대학원'
        DAT = 18, '데이터사이언스대학원'

    class PLACE_TYPE(models.TextChoices):
        ETC = 0, 'etc'
        BLD = 1, 'building'
        ATM = 2, 'atm'
        PLY = 3, 'playfield'
        PRK = 4, 'parking_lot'

    # choices 사용 예시
    #   place.type : 0
    #   place.get_type_display() : 'building'

    name = models.CharField(max_length=100, null=False)
    number = models.PositiveSmallIntegerField(null=True)
    category = models.PositiveSmallIntegerField(choices=PLACE_CATEGORY.choices, default=PLACE_CATEGORY.ETC)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='places')
    type = models.PositiveSmallIntegerField(choices=PLACE_TYPE.choices, default=PLACE_TYPE.ETC)
    information = models.CharField(max_length=500, null = True)
    tags = models.ManyToManyField(Tag, related_name='tag_places')
    
    def __str__(self):
        return self.name
