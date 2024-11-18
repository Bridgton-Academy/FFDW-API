from rest_framework import serializers
from gameTeam.models import GameTeam


class GameTeamSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    game = serializers.CharField(max_length=255)
    team = serializers.CharField(max_length=255)
    pts = serializers.IntegerField()


    def create(self, validated_data):
        """
        Create and return a new `Question` instance, given the validated data.
        """
        return GameTeam.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Question` instance, given the validated data.
        """
        instance.game = validated_data.get('game', instance.game)
        instance.team = validated_data.get('team', instance.team)
        instance.pts = validated_data.get('pts', instance.pts)
        instance.save()
        return instance