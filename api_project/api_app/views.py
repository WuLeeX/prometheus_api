from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Host
from .serializers import HostSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def host_list(request):
    """
    List all code host, or create a new snippet.
    """
    if request.method == 'GET':
        host = Host.objects.all()
        serializer = HostSerializer(host, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def host_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        host = Host.objects.get(pk=pk)
    except Host.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HostSerializer(host)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HostSerializer(host, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        host.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)