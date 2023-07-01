from django.contrib import admin

from .models import Contact, DeviceTrack, MyProject

admin.site.register(MyProject)
admin.site.register(Contact)
admin.site.register(DeviceTrack)
