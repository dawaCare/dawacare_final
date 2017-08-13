from import_export.admin import ImportExportMixin
from import_export.resources import ModelResource
from django.contrib import admin
from apps.outpatients.models import *

##### Any duplicated import export code is put here

class CountryResource(ModelResource):
    class Meta:
        model = Country

class CityResource(ModelResource):
    class Meta:
        model = City

class QuarterResource(ModelResource):
    class Meta:
        model = Quarter

class DistrictResource(ModelResource):
    class Meta:
        model = District

class RegionResource(ModelResource):
    class Meta:
        model = Region

class SpecialtyResource(ModelResource):
    class Meta:
        model = Specialty

class CertificationResource(ModelResource):
    class Meta:
        model = Certification

class DoctorResource(ModelResource):
    class Meta:
        model = Doctor

class DepartmentResource(ModelResource):
    class Meta:
        model = Department

class FacilityResource(ModelResource):
    class Meta:
        model = Facility

class AllergyResource(ModelResource):
    class Meta:
        model = Allergy

class MedicationCategoryResource(ModelResource):
    class Meta:
        model = MedicationCategory

class DiagnosisCategoriesResource(ModelResource):
    class Meta:
        model = DiagnosisCategories

class DiagnosisResource(ModelResource):
    class Meta:
        model = Diagnosis

class MedicationResource(ModelResource):
    class Meta:
        model = Medication

class OutpatientResource(ModelResource):
    class Meta:
        model = Outpatient

class EmergencyContactResource(ModelResource):
    class Meta:
        model = EmergencyContact

class VisitResource(ModelResource):
    class Meta:
        model = Visit

class MedicationReminderResource(ModelResource):
    class Meta:
        model = MedicationReminder

class CommentResource(ModelResource):
    class Meta:
        model = Outpatient

class AppointmentResource(ModelResource):
    class Meta:
        model = Appointment

class PrescribedMedResource(ModelResource):
    class Meta:
        model = PrescribedMed

class AppointmentReminderResource(ModelResource):
    class Meta:
        model = AppointmentReminder


class CommentAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = CommentResource

class CountryAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = CountryResource

class CityAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = CityResource

class QuarterAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = QuarterResource

class DistrictAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DistrictResource

class RegionAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = RegionResource

class SpecialtyAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = SpecialtyResource

class CertificationAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = CertificationResource

class DoctorAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DoctorResource

class DepartmentAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DepartmentResource

class FacilityAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = FacilityResource

class AllergyAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = AllergyResource

class MedicationCategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MedicationCategoryResource

class DiagnosisCategoriesAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DiagnosisCategoriesResource

class DiagnosisAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DiagnosisResource

class MedicationAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MedicationResource

class EmergencyContactAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = EmergencyContactResource

class VisitAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = VisitResource

class MedicationReminderAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MedicationReminderResource

class AppointmentReminderAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = AppointmentReminderResource

admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Quarter, QuarterAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(AppointmentReminder, AppointmentReminderAdmin)
admin.site.register(MedicationReminder, MedicationReminderAdmin)
admin.site.register(EmergencyContact, EmergencyContactAdmin)
admin.site.register(MedicationCategory, MedicationCategoryAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(Diagnosis, DiagnosisAdmin)
admin.site.register(DiagnosisCategories, DiagnosisCategoriesAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(Allergy, AllergyAdmin)
