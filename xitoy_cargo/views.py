from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Client, Uzbek_Db, Chine_Db, Available_party, Trek
from xitoy_cargo.serializers import ClienteSerializer, Chine_DbSerializer, Uzbek_DbSerializer, \
    Available_partySerializer, TrekSerializer


# Create your views here.
class ClientModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    search_fields = ('fullname', "telegram_id")
    filter_backends = (DjangoFilterBackend, SearchFilter)
    parser_classes = (FormParser,)
    serializer_class = ClienteSerializer
    http_method_names = ['get', 'post', 'retrieve', 'patch', 'delete']


class Uzbek_DbModelViewSet(ModelViewSet):

    search_fields = ('partiya',)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    permission_classes = [IsAuthenticated]
    queryset = Uzbek_Db.objects.all()
    serializer_class = Uzbek_DbSerializer
    parser_classes = (FormParser,)
    http_method_names = ['get', 'post', 'retrieve', 'delete']


class Chine_DbModelViewSet(ModelViewSet):
    search_fields = ("partiya")
    filter_backends = (DjangoFilterBackend, SearchFilter)

    permission_classes = [IsAuthenticated]
    queryset = Chine_Db.objects.all()
    serializer_class = Chine_DbSerializer
    parser_classes = (FormParser,)
    http_method_names = ['get', 'post', 'retrieve', 'delete']


class Available_partyModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Available_party.objects.all()
    serializer_class = Available_partySerializer
    parser_classes = (FormParser,)
    http_method_names = ['get', 'post', 'retrieve', 'patch', 'delete']

class TrekModelViewSet(ModelViewSet):
    queryset = Trek.objects.all()
    serializer_class = TrekSerializer
    parser_classes = (FormParser,)
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post',"retrieve",'delete']

