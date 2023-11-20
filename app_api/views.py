from django.shortcuts import render

from app_api.models import Movie

from app_api import serializers

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def movies_list(request):
    """
    Lista todos los proyecto, o crea un nuevo proyecto.
    """
    if request.method == 'GET':
        movies = Movie.objects.filter()
        serializer = serializers.MovieSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.MovieSerializer(data=request.data)
        if serializer.is_valid():
            #agrega mi logica
            serializer.save()
            response = {'status':'Ok',
                        'message':'Pelicula creada exitosamente',
                        'data':serializer.data}
            return Response(data= response, status=status.HTTP_201_CREATED)
        response = {'status':'Error',
                    'message':'No se pudo crear la pelicula',
                    'errors':serializer.errors}
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail(request, pk):
    """
    Muestra, actualiza o elimina una movie.
    """
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')
    if request.method == 'GET':
        serializer = serializers.MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'status':'Ok',
                        'message':'Pelicula modificada exitosamente',
                        'data':serializer.data}
            return Response(data=response)
        response = {'status':'Error',
                    'message':'No se pudo modificar la pelicula',
                    'errors':serializer.errors}
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response({'message':'Se elimino la movie'},status=status.HTTP_200_OK)
    
