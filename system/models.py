from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title
