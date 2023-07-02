from django.contrib import admin

from .models import Author, BlogPosts, Contact, DeviceTrack, MyProject, Tag

admin.site.register(MyProject)
admin.site.register(Contact)
admin.site.register(Author)
admin.site.register(BlogPosts)
admin.site.register(Tag)
admin.site.register(DeviceTrack)
