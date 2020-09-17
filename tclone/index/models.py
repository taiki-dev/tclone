from django.db import models

class NewTweet(models.Model):
    tweet = models.CharField(max_length=255)

class Like(models.Model):
    new_tweet = models.ForeignKey(NewTweet, on_delete=models.CASCADE)
