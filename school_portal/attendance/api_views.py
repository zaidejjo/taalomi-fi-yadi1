from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Absence
from .serializers import AbsenceSerializer

class AbsenceListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Return absences for the logged-in student
        if hasattr(request.user, 'student'):
            absences = Absence.objects.filter(student=request.user.student)
        else:
            absences = Absence.objects.none()
            
        serializer = AbsenceSerializer(absences, many=True)
        return Response(serializer.data)
