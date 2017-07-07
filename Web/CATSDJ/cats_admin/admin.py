from django.contrib import admin

from .models import Certification, Major, User, Space, Machine, Event

class MajorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_student_count')

class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'username', 'cuid', 'rfid', 'major', 'affiliation', 'cert_group']
    list_display = ('__str__', 'cuid', 'major', 'get_certs')
    list_filter = ['major',]
    search_fields = ['username']

class SpaceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_machine_count', 'get_certs')

class MachineAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_certs')

admin.site.register(Certification)
admin.site.register(Major, MajorAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Space, SpaceAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Event)

# Register your models here.
