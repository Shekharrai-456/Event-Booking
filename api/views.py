from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from events.models import Event
from events.serializers import EventSerializer  # You'll need to create this serializer
class EventList(APIView):
    """
    List all events or create a new event
    """
    def get(self, request):
        events = Event.objects.filter(status='approved')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organizer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class EventDetail(APIView):
    """
    Retrieve, update or delete an event instance
    """
    def get_object(self, pk):
        return get_object_or_404(Event, pk=pk)
    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    def put(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)