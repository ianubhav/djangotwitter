from django.contrib import admin

# Register your models here.
from twitterapp.models import *
from django.contrib import admin


admin.site.register(Tweet)
admin.site.register(Retweet)
admin.site.register(Follow)