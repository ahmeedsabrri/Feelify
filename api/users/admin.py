from django.contrib import admin
from .models import User , playlist, Track
# Register your models here.
admin.site.register(User)
admin.site.register(playlist)
admin.site.register(Track)