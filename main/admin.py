from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Space)
admin.site.register(UserFollowedSpaces)
admin.site.register(Post)
admin.site.register(Comment)