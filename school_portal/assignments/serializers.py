from rest_framework import serializers
from .models import Assignment, Submission, Quiz, QuizQuestion, QuizAnswer

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ['id', 'text', 'option_a', 'option_b', 'option_c', 'option_d'] # Exclude correct_option from frontend

class QuizSerializer(serializers.ModelSerializer):
    questions = QuizQuestionSerializer(source='quizquestion_set', many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = '__all__'
