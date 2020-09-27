from django.contrib import admin
from .models import tweetmodel

admin.register(tweetmodel)(admin.ModelAdmin)
# Register your models here.
