from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from game.models import Game
from game.serializers import GameSerializer


@api_view(['GET', 'POST'])
def game(request):
    """
    List all code questions, or create a new question.
    """
    if request.method == 'GET':
        game = Game.objects.all()
        serializer = GameSerializer(game, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)