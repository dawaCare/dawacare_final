from __future__ import unicode_literals
from django.db import models
from django.db.models import fields
from django.utils.encoding import python_2_unicode_compatible


from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

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




class TrackedModel(models.Model):
    # these fields are set automatically from REST requests via
    # updates from dict and the getter, setter properties, where available
    # (from the update from dict mixin)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, blank=True, null=True,
        # related_name="created_%(app_label)s_%(class)s_subrecords"
        related_name='created_by'
    )
    updated_by = models.ForeignKey(
        User, blank=True, null=True,
        # related_name="updated_%(app_label)s_%(class)s_subrecords"
        related_name='updated_by'
    )

    class Meta:
        abstract = True


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
    medication_category = models.ForeignKey(MedicationCategory)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'medications'


class NewOutpatient(TrackedModel, models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=("Date of Birth"))
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    idd = models.PositiveIntegerField(default=237)
    main_phone = models.CharField(max_length=10)
    alt_phone = models.CharField(max_length=10, blank=True, default="N/A")
    occupation = models.CharField(max_length=30, blank=True)
    address = models.ForeignKey(Address, blank=True)
    pregnant = models.BooleanField(default=False)
    signed_consent_for_roi = models.BooleanField(default=True)
    reason_for_not_signing_consent = models.TextField(blank=True)
    admitted = models.NullBooleanField()
    admission_fee = models.IntegerField(blank=True, null=True)
    consultation_fee = models.FloatField(blank=True, null=True)
    has_all_prescribed_medications = models.NullBooleanField()
    issues_with_taking_medication = models.NullBooleanField()


    # diagnoses = models.ManyToManyField(Diagnosis, null=True, blank=True)
    # allergies = models.ManyToManyField(Allergy, null=True, blank=True)
    # medications = models.ManyToManyField(Medication, through="PrescribedMed", null=True)


    def __str__(self):
        return self.surname + ', ' + self.first_name

    class Meta:
        db_table = 'newoutpatients'

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
    newoutpatient = models.ForeignKey(NewOutpatient)



    class Meta:
        db_table = 'emergency_contacts'


class PrescribedMed(models.Model):
    medication = models.ForeignKey(Medication, related_name='prescription')
    newoutpatient = models.ForeignKey(NewOutpatient, related_name='prescription')
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

    newoutpatient = models.ForeignKey(NewOutpatient)
    doctor = models.ForeignKey(Doctor)
    facility = models.ForeignKey(Facility)

    class Meta:
        db_table = 'visits'

class Appointment(models.Model):
    appt_date = models.DateTimeField()

    facility = models.ForeignKey(Facility)
    doctor = models.ForeignKey(Doctor)
    newoutpatient = models.ForeignKey(NewOutpatient)
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



#################################################################

@python_2_unicode_compatible
class Outpatient(models.Model):
    visit_date = models.CharField(max_length=100, blank=True)
    first_name = models.CharField('First Name', max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=50,blank=True)
    gender = models.CharField(max_length=20, blank=True)
    main_phone = models.BigIntegerField(null=True)
    alt_phone = models.BigIntegerField(null=True, blank=True)
    occupation = models.CharField(max_length=40, blank=True)
    address = models.CharField(max_length=200, blank=True)
    admitted = models.BooleanField(default=False)
    doctors_name = models.CharField(max_length=200, blank=True)
    doctors_note = models.TextField(null=True, blank=True)
    appt_date = models.CharField(max_length=100, blank=True)
    reminder_schedule_1_date = models.CharField(max_length=200, blank=True)
    sign_consent_for_roi = models.BooleanField(default=False)
    reason_for_not_signing_consent = models.CharField(max_length=300, blank=True)
    name_of_center = models.CharField(max_length=100, blank=True)
    patient_received_ed = models.BooleanField(default=False)
    consultation_fee = models.CharField(max_length=50, blank=True)
    admission_fee = models.IntegerField(blank=True, null=True)
    lab_fee = models.IntegerField(blank=True, null=True)
    medication_1 = models.CharField(max_length=100, blank=True)
    medication_2 = models.CharField(max_length=100, blank=True)
    medication_3 = models.CharField(max_length=100, blank=True)
    medication_4 = models.CharField(max_length=100, blank=True)
    medication_5 = models.CharField(max_length=100, blank=True)
    medication_6 = models.CharField(max_length=100, blank=True)
    medication_7 = models.CharField(max_length=100, blank=True)
    message_sent = models.TextField(blank=True)
    contacted_patient = models.BooleanField(default=False)
    patient_showed_up = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)
    has_all_medications = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    issues_with_taking_medication = models.BooleanField(default=False)
    reminder_frequency = models.CharField(max_length=300, blank=True)
    reminder_end_date = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.last_name

###################################################################
