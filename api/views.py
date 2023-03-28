from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Room
from .serializer import RoomSerializer, CreateRoomSerializer

# Create your views here.


class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CreateView(APIView):
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest = serializer.data.get('guest')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            querySet = Room.objects.filter(host=host)
            if querySet.exists():
                room = querySet[0]
                room.guest = guest
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest', 'votes_to_skip'])
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else:
                room = Room(
                    host=host, votes_to_skip=votes_to_skip, guest=guest)
                room.save()
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
