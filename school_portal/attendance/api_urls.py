from django.urls import path
from . import api_views

urlpatterns = [
    path('absences/', api_views.AbsenceListAPIView.as_view(), name='api_absence_list'),
]
