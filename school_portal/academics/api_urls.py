from django.urls import path
from . import api_views

urlpatterns = [
    path('subjects/', api_views.SubjectListAPIView.as_view(), name='api_subject_list'),
    path('subjects/<int:pk>/', api_views.SubjectDetailAPIView.as_view(), name='api_subject_detail'),
    path('lessons/<int:pk>/', api_views.LessonDetailAPIView.as_view(), name='api_lesson_detail'),
]
