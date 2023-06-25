from django.contrib import admin

from .models import Contact, MyProject

admin.site.register(MyProject)
admin.site.register(Contact)
