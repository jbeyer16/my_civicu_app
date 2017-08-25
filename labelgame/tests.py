import datetime
import doctest
import os

from my_civicu_app import bot
import my_civicu_app.settings
from django.test import TestCase
from django.utils import timezone

from .models import Image

MEDIA_ROOT = my_civicu_app.settings.MEDIA_ROOT
# Create your tests here.


class ImageModelTest(TestCase):
    fixtures = ['labelgame_test_data.json'] #, 'labelgame_user_test_data.json']
    caption = 'This is only a test ... image taken 2.5 years ago.'

    def create_image(self, caption=caption):
        return Image.objects.create(caption=caption,
                                    taken_date=(timezone.now() -
                                                datetime.timedelta(265.25
                                                                   * 2.5)),
                                    imgfile=os.path.join(MEDIA_ROOT,
                                                         'test_image.jpg'),
                                    # uploaded_date=timezone.now(),
                                    created_date=timezone.now())

    def test_image_creation(self):
        image = self.create_image()
        self.assertTrue(isinstance(image, Image))
        self.assertEqual(self.caption, image.caption)


class BotTest(TestCase):

    def test_doctests(self):
        results = doctest.testmod(bot)
        self.assertEqual(results.failed, 0)
