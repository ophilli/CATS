from django.contrib import admin

from .models import User, Machine, Event

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'user_2fa', 'year_in_school')

admin.site.register(User, UserAdmin)
admin.site.register(Machine)
admin.site.register(Event)
# Register your models here.
