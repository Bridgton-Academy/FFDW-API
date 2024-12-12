from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from round.models import Round
from round.serializers import RoundSerializer


@api_view(['GET', 'POST'])
def round(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        round = Round.objects.all()
        serializer = RoundSerializer(round, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RoundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)