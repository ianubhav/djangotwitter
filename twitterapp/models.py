from django.db import models

class Tweet(models.Model):
    user = models.ForeignKey('auth.User')
    text = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)
    def get_cname(self):
    	class_name = 'tweet'
    	return class_name 
class Retweet(models.Model):
    user = models.ForeignKey('auth.User')
    tweet = models.ForeignKey('Tweet')
    text = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)
    def get_cname(self):
    	class_name = 'retweet'
    	return class_name 

class Follow(models.Model):
    user = models.ForeignKey('auth.User', related_name='friends')
    target = models.ForeignKey('auth.User', related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'target')