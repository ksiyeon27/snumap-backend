# setup_test_data.py
# https://mattsegal.dev/django-factoryboy-dummy-data.html
  
from django.db import transaction
from django.core.management.base import BaseCommand

coords = [
    (37.4565095, 126.9500385),
    (37.4565100, 126.9500400)
]

def delete():
    models = [Room, Place, Location, Tag]
    for m in models:
        m.objects.all().delete()

@transaction.atomic
def create_place_room():
    # Create 
    l1 = Location.objects.create(latitude=coords[0][0], longitude=coords[0][1])
    l2 = Location.objects.create(latitude=coords[1][0], longitude=coords[1][1])
    tag1 = Tag.objects.create(name="윗공대")
    tag2 = Tag.objects.create(name="컴퓨터공학부")
    tag3 = Tag.objects.create(name="와플스튜디오")
    #
    # Place
    p1 = Place.objects.create(
        name = "제 1공학관", 
        number = 301, 
        category = Place.PLACE_CATEGORY.ENG, 
        location = l1,
        type = Place.PLACE_TYPE.BLD,
        information = "제 1공학관입니다."
    )
    p1.tags.add(tag1, tag2, tag3)
    p1 = Place.objects.create(
        name = "제 2공학관", 
        number = 301, 
        category = Place.PLACE_CATEGORY.ENG, 
        location = l2,
        type = Place.PLACE_TYPE.BLD,
        information = "제 2공학관입니다."
    )
    p1.tags.add(tag1)
    #
    # Room 
    r1 = Room.objects.create(
        name = "컴퓨터공학부 과방", 
        number = 317, 
        type = Room.ROOM_TYPE.CLS, 
        floor = 3,
        building = p1,
        information = "컴퓨터공학부 과방입니다. 와플스튜디오 동방이 있습니다."
    )
    r1.tags.add(tag1, tag2, tag3)
    r2 = Room.objects.create(
        name = "S-lab", 
        number = 316, 
        type = Room.ROOM_TYPE.CLS, 
        floor = 3,
        building = p1,
        information = "S-lab입니다. 컴공 과방옆입니다."
    )
    r2.tags.add(tag1, tag2)
    r3 = Room.objects.create(
        name = "전기정보공학부 과방", 
        number = 207, 
        type = Room.ROOM_TYPE.CLS, 
        floor = 2,
        building = p1,
        information = "전기정보공학부 과방입니다."
    )
    r3.tags.add(tag1, tag2)

delete()
create_place_room()