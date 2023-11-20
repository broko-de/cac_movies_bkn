from rest_framework import serializers
from app_api.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ['id','title','director','release_date','banner']
