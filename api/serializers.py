from rest_framework import serializers
from api.models import *
from rest_auth.serializers import UserDetailsSerializer

class PixelSerializer(serializers.ModelSerializer):
    class Meta :
        model = PixelModel
        fields = '__all__'

class VegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = VegetableModel
        fields = '__all__'


class GardenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GardenModel
        fields = '__all__'


class WeatherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherModel
        fields = "__all__"


class GrowModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrowModel
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = "__all__"


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelModel
        fields = "__all__"

class IrrigaiaDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrrigaiaDeviceModel
        fields=["device_id"]

# class UserSerializer(UserDetailsSerializer):
#     company_name = serializers.CharField(source="userprofile.company_name")
#
#     class Meta(UserDetailsSerializer.Meta):
#         fields = UserDetailsSerializer.Meta.fields + ('company_name',)
#
#     def update(self, instance, validated_data):
#         profile_data = validated_data.pop('userprofile', {})
#         company_name = profile_data.get('company_name')
#
#         instance = super(UserSerializer, self).update(instance, validated_data)
#
#         # get and update user profile
#         profile = instance.userprofile
#         if profile_data and company_name:
#             profile.company_name = company_name
#             profile.save()
#         return instance
