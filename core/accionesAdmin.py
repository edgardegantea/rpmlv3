import csv
from django.http import HttpResponse
from import_export.formats import base_formats
from import_export.admin import ExportMixin


# use for all admins that are admin.ModelAdmin and use ExportMixin
class AdminResource(ExportMixin):

    def get_export_formats(self):
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.ODS,
            base_formats.HTML
        )

        return [f for f in formats if f().can_export()]

    class Meta:
        abstract = True


class ExportarCsvMixin:
    def exportar_a_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    exportar_a_csv.short_description = "Exportar selección a CSV"



def get_export_formats(self):
    formats = (
      base_formats.CSV,
      base_formats.XLS,
      base_formats.XLSX,
      )

    return [f for f in formats if f().can_export()]

    class Meta:
        abstract = True