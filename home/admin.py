from django.contrib import admin

from home.models import Contact, Post, Subscribtion

# Register your models here.
admin.site.register(Contact)
admin.site.register(Subscribtion)
admin.site.register(Post)