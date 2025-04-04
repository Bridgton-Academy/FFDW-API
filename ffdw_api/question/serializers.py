from rest_framework import serializers
from question.models import Question


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question = serializers.CharField(max_length=255, required=True)
    answeronepoints = serializers.IntegerField(required=True)
    answerone = serializers.CharField(max_length=255, required=False, allow_blank=True)
    answertwopoints = serializers.IntegerField(required=True)
    answertwo = serializers.CharField(max_length=255, required=False, allow_blank=True)
    answerthreepoints = serializers.IntegerField(required=True)
    answerthree = serializers.CharField(max_length=255, required=False, allow_blank=True)
    answerfourpoints = serializers.IntegerField(required=True)
    answerfour = serializers.CharField(max_length=255, required=False, allow_blank=True)
    answerfivepoints = serializers.IntegerField(required=True)
    answerfive = serializers.CharField(max_length=255, required=False, allow_blank=True)
    answersixpoints = serializers.IntegerField(required=True)
    answersix = serializers.CharField(max_length=255, required=False, allow_blank=True)
    answersevenpoints = serializers.IntegerField(required=True)
    answerseven = serializers.CharField(max_length=255, required=False, allow_blank=True)
    answereightpoints = serializers.IntegerField(required=True)
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
        instance.answeronepoints = validated_data.get('answeronepoints', instance.answeronepoints)
        instance.answerone = validated_data.get('answerone', instance.answerone)
        instance.answertwopoints = validated_data.get('answertwopoints', instance.answertwopoints)
        instance.answertwo = validated_data.get('answertwo', instance.answertwo)
        instance.answerthreepoints = validated_data.get('answerthreepoints', instance.answerthreepoints)
        instance.answerthree = validated_data.get('answerthree', instance.answerthree)
        instance.answerfourpoints = validated_data.get('answerfourpoints', instance.answerfourpoints)
        instance.answerfour = validated_data.get('answerfour', instance.answerfour)
        instance.answerfivepoints = validated_data.get('answerfivepoints', instance.answerfivepoints)
        instance.answerfive = validated_data.get('answerfive', instance.answerfive)
        instance.answersixpoints = validated_data.get('answersixpoints', instance.answersixpoints)
        instance.answersix = validated_data.get('answersix', instance.answersix)
        instance.answersevenpoints = validated_data.get('answersevenpoints', instance.answersevenpoints)
        instance.answerseven = validated_data.get('answerseven', instance.answerseven)
        instance.answereightpoints = validated_data.get('answereightpoints', instance.answereightpoints)
        instance.answereight = validated_data.get('answereight', instance.answeright)
        instance.save()
        return instance