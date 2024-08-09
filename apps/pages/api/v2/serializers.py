from rest_framework import serializers

from apps.pages.api.v1.serializers import AboutCardSerializer, AboutPartnersSerializer, AboutImagesSerializer, \
    AboutGallerySerializer, AboutFAQSerializer, AboutFAQImageSerializer
from apps.pages.models import AboutPage, MainPage, AboutCard, AboutPartners, AboutImages, AboutGallery, AboutFAQ, \
    AboutFAQImage
from apps.prices.models import Category as PriceCategory
from apps.prices.serializers import CategorySerializer as PriceCategorySerializer
from apps.doctors.models import Doctor
from apps.doctors.serializers import DoctorListSerializer


class MainPageOurServicesSerializer(serializers.Serializer):
    our_services = serializers.SerializerMethodField(read_only=True)

    def get_our_services(self):
        obj = PriceCategory.objects.all()
        return PriceCategorySerializer(obj, many=True).data

    class Meta:
        fields = ['our_services']


class MainPageOurSpecialistsSerializer(serializers.Serializer):
    our_specialists = serializers.SerializerMethodField(read_only=True)

    def ger_our_specialists(self):
        obj = Doctor.objects.all()
        return DoctorListSerializer(obj, many=True).data

    class Meta:
        fields = ['our_specialists']


class MainPageAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = ['about_us_title', 'about_us_description']


class MainPageBirthCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = ['counter_title', 'counter_sub_title', 'birth_counter', 'birth_counter_sub_title', 'boys_counter',
                  'girls_counter']


class MainPageContactsSerializer(serializers.ModelSerializer):
    pass


# ABOUT PAGE

class AboutPageAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPage
        fields = [
            'title',
            'text',
            'image',
            'counter_1_title',
            'counter_1_value',
            'counter_2_title',
            'counter_2_value',
            'counter_3_title',
            'counter_3_value',
        ]


class AboutPageIncludeSerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField()

    def get_cards(self, obj):
        cards = AboutCard.objects.all()
        return AboutCardSerializer(cards, many=True).data

    class Meta:
        model = AboutPage
        fields = [
            'cards_title',
            'cards',
        ]


class AboutPageFAQSerializer(serializers.ModelSerializer):
    faqs = serializers.SerializerMethodField()
    faq_images = serializers.SerializerMethodField()

    class Meta:
        model = AboutPage
        fields = [
            'faq_title',
            'faqs',
            'faq_images',
        ]

    def get_faqs(self, obj):
        faqs = AboutFAQ.objects.all()
        return AboutFAQSerializer(faqs, many=True).data

    def get_faq_images(self, obj):
        faq_images = AboutFAQImage.objects.all()
        return AboutFAQImageSerializer(faq_images, many=True).data


class AboutPageParentsSerializer(serializers.ModelSerializer):
    parnters = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    def get_partners(self, obj):
        partners = AboutPartners.objects.all()
        return AboutPartnersSerializer(partners, many=True).data

    def get_images(self, obj):
        images = AboutImages.objects.all()
        return AboutImagesSerializer(images, many=True).data

    class Meta:
        model = AboutPage
        fields = [
            'parents_title',
            'parents',
            'images',
        ]


class AboutPageGallerySerializer(serializers.ModelSerializer):
    gallery = serializers.SerializerMethodField()

    def get_gallery(self, obj):
        gallery = AboutGallery.objects.all()
        return AboutGallerySerializer(gallery, many=True).data

    class Meta:
        model = AboutPage
        fields = [
            'gallery_title',
            'gallery',
        ]
