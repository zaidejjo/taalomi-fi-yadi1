from django.urls import path
from . import api_views

urlpatterns = [
    path('competitions/', api_views.CompetitionListAPIView.as_view(), name='api_competition_list'),
    path('competitions/<int:pk>/', api_views.CompetitionDetailAPIView.as_view(), name='api_competition_detail'),
]
