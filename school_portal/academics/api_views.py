from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Subject, Lesson
from .serializers import SubjectSerializer, LessonSerializer

class SubjectListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Filter subjects based on user role/grade if needed
        # For now, return all subjects or filter by student's grade
        if hasattr(request.user, 'student'):
            subjects = Subject.objects.filter(grade=request.user.student.grade)
        else:
            subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

class SubjectDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            subject = Subject.objects.get(pk=pk)
            serializer = SubjectSerializer(subject)
            return Response(serializer.data)
        except Subject.DoesNotExist:
            return Response({'error': 'Subject not found'}, status=404)

class LessonDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            lesson = Lesson.objects.get(pk=pk)
            serializer = LessonSerializer(lesson)
            return Response(serializer.data)
        except Lesson.DoesNotExist:
            return Response({'error': 'Lesson not found'}, status=404)
