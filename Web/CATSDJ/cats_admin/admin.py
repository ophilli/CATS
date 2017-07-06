from django.contrib import admin

from .models import Certification, Major, User, Space, Machine, Event

class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'username', 'cuid', 'rfid', 'major', 'affiliation', 'cert_group']
    list_display = ('__str__', 'cuid', 'major', 'get_certs')
    list_filter = ['major',]
    search_fields = ['username']

admin.site.register(Certification)
admin.site.register(Major)
admin.site.register(User, UserAdmin)
admin.site.register(Space)
admin.site.register(Machine)
admin.site.register(Event)

# Register your models here.
