from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', login_required(views.Todo.as_view()), name='users-index'),
    url(r'^contacted_patient_appt$', login_required(views.AppointmentContact.as_view()), name="contacted_patient_appt"),
    url(r'^contacted_patient_med$', login_required(views.MedicationContact.as_view()), name="contacted_patient_med"),
    url(r'^sent_med$', login_required(views.SentMed.as_view()), name='sent_med'),
    url(r'^sent_appt$', login_required(views.SentAppt.as_view()), name='sent_appt'),
    url(r'^message_med$', login_required(views.MessageMed.as_view()), name='message_med'),
    url(r'^message_appt$', login_required(views.MessageAppt.as_view()), name='message_appt'),
    url(r'^followed_up$', login_required(views.FollowedUp.as_view()), name="followed_up"),
]
