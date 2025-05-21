from rest_framework import serializers
from buisness.models import Business

class BusinessSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length= 100)
    type = serializers.CharField(max_length= 100)
    country = serializers.CharField(max_length= 100)
    state = serializers.CharField(max_length= 100)
    street = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length= 100)
    logo = serializers.ImageField()
    name = serializers.CharField(max_length= 100)


    class Meta:
        model = Business
        fields = ['id','name','logo','type','country','state','phone','street','created_at', 'city']