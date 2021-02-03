from django.shortcuts import render

# Create your views here.
from core.models import Location
from core.serializers import LocationSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

# ViewSets define the view behavior.
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def create(self, request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }
        try:
            serializer = self.get_serializer(data=request.data, context=serializer_context)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response("Marked", status=status.HTTP_201_CREATED, headers=headers)
        except:
            return Response("Already Marked", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            snippet = self.get_object(pk)
            snippet.delete()
            return Response("Removed", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Does not exist", status=status.HTTP_204_NO_CONTENT)
