from django.contrib import admin
from first_app.models import Topic, Webpage, AccessLog, User, UserProfileInfo

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessLog)
admin.site.register(User)
admin.site.register(UserProfileInfo)
