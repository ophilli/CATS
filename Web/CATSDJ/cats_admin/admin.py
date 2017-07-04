from django.contrib import admin

from .models import Certification, User, Machine, Event

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'cuid', 'rfid', 'affiliation', 'major', 'get_certs', 'join_date')

#class MachineAdmin(admin.ModelAdmin):
    #list_display = ('hostname', 'mach_type', 'mach_sn', 'mach_2fa', 'get_certs')

class EventAdmin(admin.ModelAdmin):
    list_display = ('node', 'user', 'status', 'timestamp')

admin.site.register(User, UserAdmin)
#admin.site.register(Machine, MachineAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Certification)
# Register your models here.
