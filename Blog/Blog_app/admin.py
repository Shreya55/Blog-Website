from django.contrib import admin
from .models import Post
admin.site.register(Post)

#whatever model you make in ur db, make sure to register it in admin to be able to view those models on admin pg