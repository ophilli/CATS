from django.contrib import admin

from .models import Certification, Major, User, Space, Machine, Event

admin.site.register(Certification)
admin.site.register(Major)
admin.site.register(User)
admin.site.register(Space)
admin.site.register(Machine)
admin.site.register(Event)

# Register your models here.
