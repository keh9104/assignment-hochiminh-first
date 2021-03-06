from django.db import models
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    author = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=50)
    contents = models.TextField()
    price = models.IntegerField()
    RATING = (
        (1, "★"),
        (2, "★★"),
        (3, "★★★"),
        (4, "★★★★"),
        (5, "★★★★★"),
    )
    rating = models.IntegerField(choices=RATING, default=1,)
    img = models.FileField(blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=50, default="")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()

    def __str__(self):
        return self.content
