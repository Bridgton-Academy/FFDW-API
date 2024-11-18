from rest_framework import serializers
from game.models import Game


class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    teamone = serializers.CharField(max_length=255)
    teamtwo = serializers.CharField(max_length=255)


    def create(self, validated_data):
        """
        Create and return a new `Question` instance, given the validated data.
        """
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Question` instance, given the validated data.
        """
        instance.teamone = validated_data.get('teamone', instance.teamone)
        instance.teamtwo = validated_data.get('teamtwo', instance.teamtwo)
        instance.save()
        return instance