from django.contrib import admin
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
from import_export.resources import ModelResource

from apps.outpatients.models import *

class OutpatientResource(ModelResource):

    class Meta:
        model = Outpatient

class OutpatientAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = OutpatientResource


admin.site.register(Outpatient, OutpatientAdmin)
