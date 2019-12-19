from rest_framework.response import Response
from api.models import VegetableModel,PixelModel,IrrigaiaDeviceModel
from rest_framework.permissions import IsAuthenticated  #
from rest_framework import generics
from api.serializers import VegetableSerializer,PixelSerializer,IrrigaiaDeviceSerializer
from django.conf import settings
from django.http import JsonResponse
from rest_framework import viewsets

# Create your views here.
class Weatherview(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)             #
    def get(self, request, *args, **kwargs):
        req_lat = kwargs['lat']
        req_lon = kwargs['lon']
        #queryset = PixelModel.objects.extra(where=["lat LIKE '%" + req_lat + "%'"]).extra(
        #   where=["lon LIKE '%" + req_lon + "%'"])
        #data = list(queryset.values())
        #return JsonResponse(data, safe=False)
        pass


class Pixelview(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)             #
    def get(self, request, *args, **kwargs):
       req_lat= kwargs['lat']
       req_lon = kwargs['lon']
       queryset = PixelModel.objects.extra(where=["lat LIKE '%"+req_lat+"%'"]).extra(where=["lon LIKE '%"+req_lon+"%'"])
       data=list(queryset.values())
       return JsonResponse(data, safe=False)

#    queryset = PixelModel.objects.all()
#    serializer_class = PixelSerializer

class VegetableList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)             #
    queryset = VegetableModel.objects.all()
    serializer_class = VegetableSerializer


class VegetableDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)             #
    queryset = VegetableModel.objects.all()
    serializer_class = VegetableSerializer



class VegetablePost(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)             #
    queryset = VegetableModel.objects.all()
    serializer_class = VegetableSerializer



class IrrigaiaDeviceViewset(viewsets.ModelViewSet):
    serializer_class = IrrigaiaDeviceSerializer
    queryset = IrrigaiaDeviceModel.objects.all()


class Version(generics.GenericAPIView):
    def get(self, request, format=None):
        version_num= settings.VERSION_NUM
        version_name= settings.VERSION_NAME
        return Response({ 'version_name':version_name,'version_num': version_num})