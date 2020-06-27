from rest_framework import serializers

from quiz.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('__all__',)


#class ChoiceSerializer(serializers.ModelSerializer):