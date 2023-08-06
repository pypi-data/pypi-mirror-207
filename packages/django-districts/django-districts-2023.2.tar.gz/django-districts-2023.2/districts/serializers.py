from rest_framework import serializers


from districts.models import *


# Regions Serializer Class
class Regions_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = '__all__'


# Districts Serializer Class
class Districts_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = '__all__'

# Districts ListSerializer Class
class Districts_ListSerializer(serializers.ModelSerializer):
    region = serializers.SlugRelatedField(read_only=True, slug_field="region")
    
    class Meta:
        model = Districts
        fields = '__all__'


# County Serializer Class
class County_Serializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = '__all__'


# County ListSerializer Class
class County_ListSerializer(serializers.ModelSerializer):
    district = serializers.SlugRelatedField(read_only=True, slug_field="district")

    class Meta:
        model = County
        fields = '__all__'


# SubCounty Serializer Class
class SubCounty_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SubCounty
        fields = '__all__'


# SubCounty ListSerializer Class
class SubCounty_ListSerializer(serializers.ModelSerializer):
    county = serializers.SlugRelatedField(read_only=True, slug_field="county")

    class Meta:
        model = SubCounty
        fields = '__all__'


# Parish Serializer Class
class Parish_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Parish
        fields = '__all__'


# Parish ListSerializer Class
class Parish_ListSerializer(serializers.ModelSerializer):
    sub_county = serializers.SlugRelatedField(read_only=True, slug_field="sub_county")

    class Meta:
        model = Parish
        fields = '__all__'


# Location Serializer Class
class Location_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
