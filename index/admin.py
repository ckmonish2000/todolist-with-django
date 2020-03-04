from django.contrib import admin

# Register your models here.
from .models import bus,buststops


admin.site.register(bus)
admin.site.register(buststops)