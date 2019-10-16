from django.contrib import admin
from .models import *

class ShowAdmin(admin.ModelAdmin):
	list_display = ('title', 'network', 'id')

admin.site.register(Show, ShowAdmin)