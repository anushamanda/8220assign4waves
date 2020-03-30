from django.contrib import admin

from .models import Supervisor

class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'employee_id', 'email')


admin.site.register(Supervisor, SupervisorAdmin)
