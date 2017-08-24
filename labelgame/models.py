# import datetime
# import os

from django.contrib.auth.models import User
from django.db import models
# from django.utils import timezone


"""

Profile model with first and last name an image or profile description
Label model with image ID and classification and user id
Image model with image ID and path to the image on a shared server or a binary
    blob of the image itself

"""
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def __str__(self):
#         return self.question_text

#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text


class Image(models.Model):
    """ A database record for uploaded images to be labeled """
    caption = models.CharField("Description of the image, where and when it "
                               "was taken", max_length=512, default=None,
                               blank=True, null=True)
    uploaded_by = models.ForeignKey(User, default=None, null=True)
    imgfile = models.FileField("Select image to upload ",
                               upload_to='images/', blank=True, default=None)
    created_date = models.DateTimeField('Date photo was created.',
                                        auto_now_add=True, blank=True,
                                        null=True)
    taken_date = models.DateTimeField('Date photo was taken.', null=True, 
                                      default=None)
    #updated_date = models.DateTimeField('Date photo was changed.', 
    #                                    auto_now=True)

    def __str__(self):
        return str(self.imgfile) + ' ' + str(self.caption)


class UserLabel(models.Model):
    """ Individual user labels (their filled out ballot, voting for a label for
    an image) """
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, default=None, null=True)


class TotalVotes(models.Model):
    """ Aggregated votes (by all users, who are allowed to vote multiple times)
    for an individual image """
    image = models.ForeignKey(Image, default=None, null=True)
    name = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)
