from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import View
from apps.outpatients.models import *
from django.contrib.auth.models import User
# Create your views here.

class Todo(View):
    def get(self, request):
        print(request.user.id)
        print(MedicationReminder.objects.all())
        print(AppointmentReminder.objects.all())
        # med_todos = MedicationReminder.objects.get(user=request.user.id)
        # print(med_todos)
        med_todos = MedicationReminder.objects.filter(pcc=request.user.id).order_by('date')
        appt_todos = AppointmentReminder.objects.filter(pcc=request.user.id).order_by('date')
        context = {
            'med_todos' : med_todos,
            'appt_todos' : appt_todos,
        }
        return render(request, 'outpatients/index.html', context)

class AppointmentContact(View):
    def post(self, request):
        print (request.POST)
        appt_rem = AppointmentReminder.objects.get(id=request.POST['appt_id'])
        print(appt_rem)
        print(appt_rem.appt_date.appt_date)
        appt_rem.contacted_patient = "True"
        print(appt_rem.contacted_patient)
        appt_rem.save()
        return redirect('/')

class MedicationContact(View):
    def post(self, request):

        med_rem = MedicationReminder.objects.get(id=request.POST['med_id'])
        print(med_rem)

        med_rem.contacted_patient = "True"

        med_rem.save()
        return redirect('/')

class SentMed(View):
    def post(self, request):
        print (request.POST)

        med_rem = MedicationReminder.objects.get(id=request.POST['med_id'])

        med_rem.sent = "True"

        med_rem.save()
        return redirect('/')


class SentAppt(View):
    def post(self, request):
        print (request.POST)

        appt_rem = AppointmentReminder.objects.get(id=request.POST['appt_id'])

        appt_rem.sent = "True"

        appt_rem.save()
        return redirect('/')

class MessageMed(View):
    def post(self, request):
        print (request.POST)

        med_rem = MedicationReminder.objects.get(id=request.POST['med_id'])

        med_rem.message = request.POST['med_message']

        print (med_rem.message)

        med_rem.save()
        return redirect('/')

class MessageAppt(View):
    def post(self, request):
        print(request.POST)

        appt_rem = AppointmentReminder.objects.get(id=request.POST['appt_id'])

        appt_rem.message = request.POST['appt_message']
        print (appt_rem.message)
        appt_rem.save()
        return redirect('/')

class FollowedUp(View):
    def post(self, request):
        print (request.POST)

        appt_rem = AppointmentReminder.objects.get(id=request.POST['appt_id'])
        appt = appt_rem.appt_date

        appt.followed_up = True

        appt.save()
        return redirect('/')
