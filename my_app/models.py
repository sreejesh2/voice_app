from django.db import models

# Create your models here.
class FeedBack(models.Model):
    name = models.CharField(max_length=100)
    feed_back_text = models.TextField()
    phone_number = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
