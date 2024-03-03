from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import *
from app.serializers import ProductSerializer, LessonSerializer


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LessonAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        queryset = Lesson.objects.all()
        student_id = self.request.query_params.get('student_id', None)
        product_id = self.request.query_params.get('product_id', None)
        queryset = queryset.filter(pr__pk=product_id, pr__access__student_id=student_id, pr__access__value=True)
        return queryset

