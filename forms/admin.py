from django.contrib import admin

from .models import Forms, Record_log, Record, Station

class FormAdmin(admin.ModelAdmin):
    list_display = ('id', 'form_title', 'created_date', 'is_published', 'published_date', )
    list_display_links = ('id', 'form_title')
    list_filter = ('form_title',)
    list_editable = ('is_published',)

class Record_logAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'form_name', 'uploaded_date',)
    list_display_links = ('id', 'name', 'form_name',)
    list_filter = ('form_name',)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'form_name','status', 'created_date',)
    list_display_links = ('id', 'name', 'form_name',)
    list_filter = ('name', 'form_name',)


class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'station_name', 'zipcode',)
    list_display_links = ('id', 'station_name',)
    list_filter = ('station_name',)



admin.site.register(Forms, FormAdmin)
admin.site.register(Record_log, Record_logAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Station, StationAdmin)