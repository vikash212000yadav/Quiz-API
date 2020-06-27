from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from quiz.models import Category, Quiz
from quiz.serializers import CategorySerializer, QuestionSerializer


class ListCategories(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class StartQuiz(APIView):

    def get(self, request, category_id=None):
        try:
            quiz = Quiz.objects.get(category__id=category_id)
        except Quiz.DoesNotExist:
            raise Http404

        serializer = QuestionSerializer(quiz.question.all(), many=True)
        return Response(serializer.data)