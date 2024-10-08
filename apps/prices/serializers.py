from rest_framework import serializers
from .models import Service, Packages, Category, PackageService, PackageServiceType
from apps.services.models import Type
from apps.services.serializers import TypeSerializer


class CategorySerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'services']

    def get_services(self, obj):
        return ServiceSerializer(Service.objects.filter(category=obj), many=True).data


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'price', 'tooltip']


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__'


class PackageServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageService
        fields = '__all__'


class PackageServicesTypeSerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField()

    class Meta:
        model = PackageServiceType
        fields = '__all__'

    def get_services(self, obj):
        return PackageServicesSerializer(PackageService.objects.filter(type=obj), many=True).data


class PreiskurantSerializer(serializers.Serializer):
    packeges = serializers.SerializerMethodField()
    types = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    service_types = serializers.SerializerMethodField()

    def get_packeges(self, obj):
        request = self.context.get('request')
        return PackageSerializer(Packages.objects.all(), many=True, context={'request': request}).data

    def get_types(self, obj):
        return PackageServicesTypeSerializer(PackageServiceType.objects.all(), many=True).data

    def get_services(self, obj):
        return ServiceSerializer(Service.objects.all(), many=True).data

    def get_service_types(self, obj):
        return CategorySerializer(Category.objects.all(), many=True).data

    class Meta:
        model = Packages
        fields = '__all__'
