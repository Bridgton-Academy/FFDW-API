from rest_framework import serializers
from round.models import Round


class RoundSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question = serializers.CharField(max_length=255)
    pts_revealed = serializers.CharField(max_length=255)
    questions_revealed = serializers.CharField(max_length=255)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return Round.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.question = validated_data.get('question', instance.question)
        instance.pts_revealed = validated_data.get('pts_revealed', instance.pts_revealed)
        instance.questions_revealed = validated_data.get('questions_revealed', instance.questions_revealed)
        instance.save()
        return instance