from django.contrib import admin
from tracking.models import PlayHub
from extended_filters.filters import DateRangeFilter
import csv
from django.http import HttpResponse


# Register your models here.


class PlayHubAdmin(admin.ModelAdmin):
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = ['user_info',
                       'time_stamp',
                       'platform_type',
                       'action',
                       'add_id']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

    search_fields = (
        'user_info',
        'action',

    )
    list_display = (
        'user_info',
        'time_stamp',
        'platform_type',
        'action',
        'add_id'
    )
    list_filter = (
        'time_stamp',
        ('time_stamp', DateRangeFilter),
        'platform_type',
    )
    actions = ["export_as_csv"]

    class Meta:
        model = PlayHub


admin.site.register(PlayHub, PlayHubAdmin)
