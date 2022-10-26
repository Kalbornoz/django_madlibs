from django.db import models

# Create your models here.


class Story(models.Model):
    def __str__(self):
        return self.story_name
    story_name = models.CharField(max_length=100)
    story_content = models.CharField(max_length=2000)


class FillIns(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)
    field4 = models.CharField(max_length=100)
    field5 = models.CharField(max_length=100)
    field6 = models.CharField(max_length=100)
    field7 = models.CharField(max_length=100)
