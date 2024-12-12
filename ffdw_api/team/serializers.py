from rest_framework import serializers
from team.models import Team


class TeamSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=True)
    users = serializers.CharField(max_length=255, required=True)
    


    def create(self, validated_data):
        """
        Create and return a new `Question` instance, given the validated data.
        """
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Question` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.users = validated_data.get('users', instance.users)
        
        instance.save()
        return instance