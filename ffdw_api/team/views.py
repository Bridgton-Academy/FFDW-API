from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from team.models import Team
from team.serializers import TeamSerializer


@api_view(['GET', 'POST'])
def team(request):
    """
    List all code questions, or create a new question.
    """
    if request.method == 'GET':
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)