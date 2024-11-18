from rest_framework import serializers
from question.models import Question


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question = serializers.CharField(max_length=255, required=True)
    answerone = serializers.CharField(max_length=255, required=False, allow_blank=True)
    answertwo = serializers.CharField(max_length=255, required=False, allow_blank=True)
    answerthree = serializers.CharField(max_length=255, required=False, allow_blank=True)
    answerfour = serializers.CharField(max_length=255, required=False, allow_blank=True)
    answerfive = serializers.CharField(max_length=255, required=False, allow_blank=True)
    answersix = serializers.CharField(max_length=255, required=False, allow_blank=True)
    answerseven = serializers.CharField(max_length=255, required=False, allow_blank=True)
    answereight = serializers.CharField(max_length=255, required=False, allow_blank=True)


    def create(self, validated_data):
        """
        Create and return a new `Question` instance, given the validated data.
        """
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Question` instance, given the validated data.
        """
        instance.question = validated_data.get('question', instance.question)
        instance.answerone = validated_data.get('answerone', instance.answerone)
        instance.answertwo = validated_data.get('answertwo', instance.answertwo)
        instance.answerthree = validated_data.get('answerthree', instance.answerthree)
        instance.answerfour = validated_data.get('answerfour', instance.answerfour)
        instance.answerfive = validated_data.get('answerfive', instance.answerfive)
        instance.answersix = validated_data.get('answersix', instance.answersix)
        instance.answerseven = validated_data.get('answerseven', instance.answerseven)
        instance.answereight = validated_data.get('answereight', instance.answeright)
        instance.save()
        return instance