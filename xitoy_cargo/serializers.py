from rest_framework import serializers
from .models import Client,Chine_Db,Uzbek_Db,Available_party,Trek
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
class Chine_DbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chine_Db
        fields = '__all__'
class Uzbek_DbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uzbek_Db
        fields = '__all__'
class Available_partySerializer(serializers.ModelSerializer):
    class Meta:
        model = Available_party
        fields = '__all__'
class TrekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trek
        fields = '__all__'
