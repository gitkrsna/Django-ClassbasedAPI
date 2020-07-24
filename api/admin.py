from django.contrib import admin
from .models import Music
# Register your models here.
class MusicAdmin(admin.ModelAdmin):
    class Meta:
        model = Music
admin.site.register(Music, MusicAdmin)