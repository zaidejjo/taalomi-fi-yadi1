from django.urls import path
from . import api_views

urlpatterns = [
    path('assignments/', api_views.AssignmentListAPIView.as_view(), name='api_assignment_list'),
    path('assignments/<int:pk>/', api_views.AssignmentDetailAPIView.as_view(), name='api_assignment_detail'),
    path('quizzes/', api_views.QuizListAPIView.as_view(), name='api_quiz_list'),
    path('quizzes/<int:pk>/', api_views.QuizDetailAPIView.as_view(), name='api_quiz_detail'),
]
