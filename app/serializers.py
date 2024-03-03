from rest_framework import serializers


from app.models import *



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('title', 'link')

class ProductSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ('title', 'owner', 'start_time', 'price', 'lessons')


