from __future__ import unicode_literals
from django.db import models
from django.db.models import fields
from django.utils.encoding import python_2_unicode_compatible
import datetime


from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


# class ConvertingDateTimeField(models.DateTimeField):
#
#     def get_prep_value(self, value):
#         return str(datetime.strptime(value, '%d-%m-%Y'))


class Country(models.Model):
    country = models.CharField(max_length=70)

    class Meta:
        db_table = 'countries'

    def __str__(self):
        return self.country

class City(models.Model):
    city = models.CharField(max_length=70)
    country = models.ForeignKey(Country)
    # updated_at = models.DateTimeField()

    class Meta:
        db_table = 'cities'

    def __str__(self):
        return self.city

class Quarter(models.Model):
    quarter = models.CharField(max_length=70)

    class Meta:
        db_table = 'quarters'

    def __str__(self):
        return self.quarter

class Address(models.Model):
    address1 = models.CharField("Address Line 1", max_length=1024)
    address2 = models.CharField("Address Line 2", max_length=1024, blank=True)
    district = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    city = models.ForeignKey(City)
    quarter = models.ForeignKey(Quarter)

    def __str__(self):
        return self.address1

    class Meta:
        db_table = 'addresses'




# class TrackedModel(models.Model):
#     created = models.DateTimeField(blank=True, null=True)
#     updated = models.DateTimeField(blank=True, null=True)
#     created_by = models.ForeignKey(
#         User, blank=True, null=True,
#         related_name='created_by'
#     )
#     updated_by = models.ForeignKey(
#         User, blank=True, null=True,
#         related_name='updated_by'
#     )
#
#     class Meta:
#         abstract = True


class Specialty(models.Model):
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'specialties'

class Certification(models.Model):
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'certifications'

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    main_phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.ForeignKey(Address)

    certifications = models.ManyToManyField(Certification)
    specialties = models.ManyToManyField(Specialty)

    class Meta:
        db_table = 'doctors'

    def __str__(self):
        return self.last_name

class Department(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'departments'

    def __str__(self):
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, blank=True)
    address = models.ForeignKey(Address, blank=True)
    departments = models.ManyToManyField(Department, blank=True)

    class Meta:
        db_table = 'facilities'

    def __str__(self):
        return self.name

class Allergy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'allergies'

class MedicationCategory(models.Model):
    category = models.CharField(max_length=50)

    class Meta:
        db_table = 'medication_categories'

    def __str__(self):
        return self.category


class DiagnosisCategories(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'diagnosis_categories'

    def __str__(self):
        return self.name

class Diagnosis(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(DiagnosisCategories)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'diagnoses'


class Medication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    medication_category = models.ForeignKey(MedicationCategory, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'medications'


class Outpatient(models.Model):
    first_name = models.CharField(max_length=255, blank=True, validators=[alphanumeric])
    surname = models.CharField(max_length=255, validators=[alphanumeric])
    middle_name = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=("Date of Birth"))
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    main_phone = models.CharField(validators=[phone_regex], max_length=15)
    alt_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    occupation = models.CharField(max_length=30, blank=True)
    address = models.ForeignKey(Address, blank=True, null=True)
    pregnant = models.BooleanField(default=False)
    signed_consent_for_roi = models.BooleanField(default=True)
    reason_for_not_signing_consent = models.TextField(blank=True)
    admitted = models.NullBooleanField()
    admission_fee = models.IntegerField(blank=True, null=True)
    consultation_fee = models.FloatField(blank=True, null=True)
    has_all_prescribed_medications = models.NullBooleanField()
    issues_with_taking_medication = models.NullBooleanField()


    diagnoses = models.ManyToManyField(Diagnosis, blank=True)
    allergies = models.ManyToManyField(Allergy, blank=True)
    medications = models.ManyToManyField(Medication, through="PrescribedMed")

    def get_diagnoses(self):
        # return self.diagnoses.all()
        return "\n".join([d.name for d in self.diagnoses.all()])

    get_diagnoses.short_description = 'Diagnoses'

    def get_meds(self):
        # return self.medications.all()
        return "\n".join([m.name for m in self.medications.all()])

    get_meds.short_description = 'Prescribed Meds'

    def get_visits(self):

        visits = Visit.objects.filter(outpatient=self.id)
        print (visits)
        strvisits = ""
        for visit in visits:
            print (visit.visit_date)
            v = str(visit.visit_date)
            print ("printing visit")
            strvisits += v + ' '
            print (strvisits)

        return strvisits

    def __str__(self):
        return self.surname + ', ' + self.first_name

    class Meta:
        db_table = 'outpatients'

class EmergencyContact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    main_phone = models.CharField(max_length=10)
    alt_phone = models.CharField(max_length=10, blank=True)
    RELATIONSHIP_CHOICES = (
        ('Sib', 'Sibling'),
        ('M', 'Mother'),
        ('F', 'Father'),
        ('C', 'Cousin'),
        ('F', 'Friend'),
        ('D', 'Daughter'),
        ('S', 'Son'),
    )
    relationship = models.CharField(max_length=10, choices=RELATIONSHIP_CHOICES, blank=True)
    address = models.ForeignKey(Address, blank=True)
    outpatient = models.ForeignKey(Outpatient)



    class Meta:
        db_table = 'emergency_contacts'


class PrescribedMed(models.Model):
    medication = models.ForeignKey(Medication, related_name='prescription')
    outpatient = models.ForeignKey(Outpatient, related_name='prescription')
    dosage_num = models.IntegerField()
    route = models.CharField(max_length=10)
    frequency = models.CharField(max_length=10)
    dosage_unit = models.CharField(max_length=10)
    end_date = models.DateField(null=True)



    class Meta:
        db_table = 'prescribedmeds'

class Visit(models.Model):
    visit_date = models.DateTimeField()
    doctors_note = models.TextField(blank=True)
    patient_received_ed = models.BooleanField(default=False)
    lab_fee = models.FloatField(blank=True)

    outpatient = models.ForeignKey(Outpatient)
    doctor = models.ForeignKey(Doctor)
    facility = models.ForeignKey(Facility)

    class Meta:
        db_table = 'visits'

class Appointment(models.Model):
    appt_date = models.DateTimeField()

    facility = models.ForeignKey(Facility)
    doctor = models.ForeignKey(Doctor)
    outpatient = models.ForeignKey(Outpatient)
    department = models.ForeignKey(Department)
    visit = models.ForeignKey(Visit)

    followed_up = models.BooleanField(default=False)

    class Meta:
        db_table = 'appointments'



class MedicationReminder(models.Model):
    prescribed_med = models.ForeignKey(PrescribedMed)
    pcc = models.ForeignKey(User, null=True)

    contacted_patient = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    message = models.TextField(blank=True)

    date = models.DateField()

    class Meta:
        db_table = 'med_reminders'

class AppointmentReminder(models.Model):
    appt_date = models.ForeignKey(Appointment)
    pcc = models.ForeignKey(User)

    contacted_patient = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    message = models.TextField(blank=True)

    date = models.DateField()


    class Meta:
        db_table = 'appt_reminders'


class Comment(models.Model):
    comment = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.comment
