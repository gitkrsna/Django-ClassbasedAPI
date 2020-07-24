from rest_framework import serializers
from api.models import Music
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['title', 'singer']


   

