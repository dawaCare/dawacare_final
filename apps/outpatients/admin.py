from django.contrib import admin
from import_export.admin import ImportExportMixin
from django.contrib.contenttypes.admin import GenericStackedInline
from apps.outpatients.models import *
from apps.outpatients.forms import *
from apps.outpatients.before_adminimportexport import *

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

class CommentInline(GenericStackedInline):
    model = Comment
    ct_field = "content_type"
    ct_fk_field = "object_id"
    fk_name = "content_object"
    extra = 0

class AppointmentAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = AppointmentResource
    inlines = [CommentInline]

class PrescribedMedAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = PrescribedMedResource
    inlines = [CommentInline]

class AppointmentReminderInline(NestedStackedInline):
    model = AppointmentReminder
    extra = 1

class AppointmentInline(NestedStackedInline):
    model = Appointment
    extra = 1
    inlines = [AppointmentReminderInline]

class VisitInline(NestedStackedInline):
    model = Visit
    extra = 1
    inlines = [AppointmentInline]

    def get_queryset(self, request):
        qs = super(VisitInline, self).get_queryset(request)
        # qs.order_by('-created_at')
        return qs

class EmergencyContactInline(NestedStackedInline):
    model = EmergencyContact
    extra = 1

class MedicationReminderInline(NestedStackedInline):
    model = MedicationReminder
    extra = 1

class PrescribedMedInline(NestedStackedInline):
    model = PrescribedMed
    extra = 1
    inlines = [MedicationReminderInline]

class OutpatientAdmin(ImportExportMixin, NestedModelAdmin):
    resource_class = OutpatientResource
    extra = 1
    fk_name = 'Outpatient'
    inlines = [PrescribedMedInline, EmergencyContactInline, VisitInline]
    list_display = ('surname', 'first_name', 'date_of_birth', 'address1', 'get_diagnoses', 'get_meds', 'get_visits')
    search_fields = ['surname', 'first_name']
    # list_filter = ['surname']
    # list_display_links = ['get_diagnoses', 'surname']

##For checking doctor uniqueness
# class DoctorAdmin(admin.ModelAdmin):
#     form = DoctorAdminForm


admin.site.register(Outpatient, OutpatientAdmin)
admin.site.register(PrescribedMed, PrescribedMedAdmin)
admin.site.register(Appointment, AppointmentAdmin)
