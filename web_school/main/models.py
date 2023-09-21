from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    accesses = models.ManyToManyField(User, through='Access', related_name='products_accessed')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title


class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_granted = models.BooleanField(default=False)
    last_access_date = models.DateTimeField(null=True, blank=True)


class LessonWatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)
    watch_time_seconds = models.IntegerField(default=0)
    last_watched_date = models.DateTimeField(null=True, blank=True)

