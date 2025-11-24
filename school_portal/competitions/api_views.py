from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Competition
from .serializers import CompetitionSerializer

class CompetitionListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        competitions = Competition.objects.all()
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(serializer.data)

class CompetitionDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            competition = Competition.objects.get(pk=pk)
            serializer = CompetitionSerializer(competition)
            return Response(serializer.data)
        except Competition.DoesNotExist:
            return Response({'error': 'Competition not found'}, status=404)
