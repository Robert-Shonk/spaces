from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Space)
admin.site.register(UserFollowedSpace)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Moderator)
admin.site.register(PostUpvote)
admin.site.register(PostDownvote)
admin.site.register(PostFunny)
admin.site.register(PostHelpful)