from django.contrib import admin
from .models import Person, Group
# Register your models here.
admin.site.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'display_group')

admin.site.register(Group)