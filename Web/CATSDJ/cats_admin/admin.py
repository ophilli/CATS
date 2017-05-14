from django.contrib import admin

from .models import User, Machine, Event

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'user_2fa', 'year_in_school')

class MachineAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'mach_type', 'mach_sn', 'mach_2fa')

class EventAdmin(admin.ModelAdmin):
    list_display = ('mach_hostname', 'cuid', 'status', 'timestamp')

admin.site.register(User, UserAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Event, EventAdmin)
# Register your models here.
