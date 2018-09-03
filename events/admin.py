from django.contrib import admin
from .models import Event, Image, Tag, Assistant
# Register your models here.
admin.site.register(Event)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Assistant)
