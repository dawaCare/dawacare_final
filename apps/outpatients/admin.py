from django.contrib import admin
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
from import_export.resources import ModelResource
from django.contrib.contenttypes.admin import GenericStackedInline
from apps.outpatients.models import *

from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class CommentInline(GenericStackedInline):
    model = Comment
    ct_field = "content_type"
    ct_fk_field = "object_id"
    fk_name = "content_object"
    extra = 0

class AppointmentAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

class PrescribedMedAdmin(admin.ModelAdmin):
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

class OutpatientAdmin(NestedModelAdmin):
    model = Outpatient
    extra = 1
    fk_name = 'Outpatient'
    inlines = [PrescribedMedInline, EmergencyContactInline, VisitInline]
    list_display = ('surname', 'first_name', 'date_of_birth', 'address', 'get_diagnoses', 'get_meds', 'get_visits')
    search_fields = ['surname', 'first_name']


admin.site.register(Outpatient, OutpatientAdmin)
admin.site.register(EmergencyContact)
admin.site.register(MedicationCategory)
admin.site.register(Medication)
admin.site.register(PrescribedMed, PrescribedMedAdmin)
admin.site.register(Diagnosis)
admin.site.register(DiagnosisCategories)
admin.site.register(Visit)
admin.site.register(Allergy)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Facility)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Specialty)
admin.site.register(Certification)
admin.site.register(AppointmentReminder)
admin.site.register(MedicationReminder)
admin.site.register(Comment)
admin.site.register(Address)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Quarter)
