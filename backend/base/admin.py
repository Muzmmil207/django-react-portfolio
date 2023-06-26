from django.contrib import admin

from .models import Contact, DeviceTrack, MyProject, Post, PostSource

admin.site.register(MyProject)
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(PostSource)
admin.site.register(DeviceTrack)
