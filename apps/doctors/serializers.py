from rest_framework import serializers
from .models import Doctor, Position, Specialization, Сertificate, Review, Photo, Order


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Сertificate
        fields = ('name', 'image')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('image',)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('image',)


class DoctorListSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()
    specialization = serializers.SerializerMethodField()

    def get_position(self, obj):
        return obj.position.name

    def get_specialization(self, obj):
        return obj.specialization.name

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'position', 'specialization', 'seniority', 'image',)


class DoctorDetailSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()
    specialization = serializers.SerializerMethodField()
    certificates = CertificateSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ('name', 'image', 'position', 'specialization', 'seniority', 'description', 'certificates', 'reviews', 'photos')

    def get_position(self, obj):
        return obj.position.name

    def get_specialization(self, obj):
        return obj.specialization.name


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
