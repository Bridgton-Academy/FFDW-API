from rest_framework import serializers
from question.models import Question


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question = serializers.CharField(max_length=255)
    answerone = serializers.CharField(max_length=255)
    answertwo = serializers.CharField(max_length=255)
    answerthree = serializers.CharField(max_length=255)
    answerfour = serializers.CharField(max_length=255)
    answerfive = serializers.CharField(max_length=255)
    answersix = serializers.CharField(max_length=255)
    answerseven = serializers.CharField(max_length=255)
    answereight = serializers.CharField(max_length=255)


    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.joined_date = validated_data.get('joined_date', instance.joined_date)
        instance.save()
        return instance