from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Assignment, Quiz, Submission
from .serializers import AssignmentSerializer, QuizSerializer, SubmissionSerializer

class AssignmentListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Filter by student's grade/subject if needed
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

class AssignmentDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            assignment = Assignment.objects.get(pk=pk)
            serializer = AssignmentSerializer(assignment)
            return Response(serializer.data)
        except Assignment.DoesNotExist:
            return Response({'error': 'Assignment not found'}, status=404)

class QuizListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)

class QuizDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            quiz = Quiz.objects.get(pk=pk)
            serializer = QuizSerializer(quiz)
            return Response(serializer.data)
        except Quiz.DoesNotExist:
            return Response({'error': 'Quiz not found'}, status=404)
