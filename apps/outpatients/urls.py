from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Todo.as_view(), name='users-index'),
    url(r'^contacted_patient_appt$', views.AppointmentContact.as_view(), name="contacted_patient_appt"),
    url(r'^contacted_patient_med$', views.MedicationContact.as_view(), name="contacted_patient_med"),
    url(r'^sent_med$', views.SentMed.as_view(), name='sent_med'),
    url(r'^sent_appt$', views.SentAppt.as_view(), name='sent_appt'),
    url(r'^message_med$', views.MessageMed.as_view(), name='message_med'),
    url(r'^message_appt$', views.MessageAppt.as_view(), name='message_appt'),
    url(r'^followed_up$', views.FollowedUp.as_view(), name="followed_up"),
]
