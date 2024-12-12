from rest_framework import serializers
from gameTeam.models import GameTeam


class GameTeamRoundSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    gameTeam = serializers.CharField(max_length=255)
    round = serializers.CharField(max_length=255)
    pts = serializers.IntegerField()
    strikes = serializers.IntegerField()


    def create(self, validated_data):
        """
        Create and return a new `Question` instance, given the validated data.
        """
        return GameTeamRound.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Question` instance, given the validated data.
        """
        instance.gameTeam = validated_data.get('game', instance.game)
        instance.round = validated_data.get('team', instance.team)
        instance.pts = validated_data.get('pts', instance.pts)
        instance.strikes = validated_data.get('strikes', instance.strikes)
        instance.save()
        return instance