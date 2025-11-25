from django.urls import path
from . import views

app_name = 'academics'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # المواد
    path('subjects/', views.subjects_view, name='subjects'),
    path('subjects/<int:grade_number>/<str:subject_name>/', views.subject_detail_view, name='subject_detail'),

    # الدروس
    path('lesson/<int:lesson_id>/', views.LessonDetailView.as_view(), name='lesson_detail'),

    # فيديو الدرس
    path('grades/<int:grade_number>/subjects/<str:subject_name>/lesson/<int:lesson_number>/video/',
         views.lesson_video_view, name='lesson_video'),

    # الجدول
    path('timetable/', views.timetable_view, name='timetable'),

    # الامتحانات
    path('exams/', views.ExamListView.as_view(), name='exams'),

    # الدرجات
    path('grades/', views.GradeListView.as_view(), name='grades'),
]
