from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gameTeam.models import GameTeam
from gameTeam.serializers import GameTeamSerializer


@api_view(['GET', 'POST'])
def gameTeam(request):
    """
    List all code questions, or create a new question.
    """
    if request.method == 'GET':
        gameTeam = GameTeam.objects.all()
        serializer = GameTeamSerializer(gameTeam, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GameTeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)