from django.test import TestCase
from rest_framework import status
from factory.django import DjangoModelFactory

from user.models import User
from user.serializers import jwt_token_of
from place.tests import PlaceFactory, TagFactory, LocationFactory
from room.tests import RoomFactory

class SearchTestCase(TestCase):
    @classmethod
    def setUp(cls):

        cls.location1 = LocationFactory(
            latitude = 143,
            longitude = 38
        )
        
        cls.tag1 = TagFactory(
            name = "301동"
        )
        
        cls.tag2 = TagFactory(
            name = "와플스튜디오 동방"
        )
        
        cls.tag3 = TagFactory(
            name = "컴퓨터공학부"
        )
        
        cls.tag4 = TagFactory(
            name = "전기정보공학부"
        )
        
        cls.tag5 = TagFactory(
            name = "기계공학부"
        )
        
        cls.place1 = PlaceFactory(
            name = "제1공학관",
            number = 301,
            category  = 6,
            location = cls.location1,
            type = 1,
        )
        
        cls.place1.tags.add(cls.tag1, cls.tag2, cls.tag3, cls.tag4, cls.tag5)
        cls.place1.save()
        
        cls.room1 = RoomFactory(
            name = "컴퓨터공학부 과방",
            type = 0,
            building = cls.place1,
        )
        
        cls.room1.tags.add(cls.tag1, cls.tag2, cls.tag3)
        cls.room1.save()
        
    def test_get_place(self):
        response = self.client.get("/search/?keyword=컴퓨터공학부&modelType=place", data={})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], 1)
        self.assertEqual(response.data[0]["name"], "제1공학관")
        
    def test_get_room(self):
        response = self.client.get("/search/?keyword=컴퓨터공학부&modelType=room", data={})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], 1)
        self.assertEqual(response.data[0]["name"], "컴퓨터공학부 과방")
        
    def test_get_both_1(self):
        response = self.client.get("/search/?keyword=컴퓨터공학부", data={})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)
        
        room = response.data[0]
        self.assertEqual(room["id"], 1)
        self.assertEqual(room["name"], "컴퓨터공학부 과방")
        self.assertEqual(room["modelType"], "room")
        
        place = response.data[1]
        self.assertEqual(place["id"], 1)
        self.assertEqual(place["name"], "제1공학관")
        self.assertEqual(place["modelType"], "place")
        
    def test_get_both_2(self):
        response = self.client.get("/search/?keyword=기계공학부", data={})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)
        place = response.data[0]
        self.assertEqual(place["id"], 1)
        self.assertEqual(place["name"], "제1공학관")
        self.assertEqual(place["modelType"], "place")
        