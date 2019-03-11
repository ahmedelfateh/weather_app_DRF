from rest_framework import serializers

from weather.models import City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = [
            'user',
            'id',
            'city',
        ]
        read_only_fields = ['user']

    def validate(self, data):
        city = data.get('city', None)
        if city == "":
            city = None
        if city is None:
            raise serializers.ValidationError('City needed')
        return data

    def validate_city(self, value):
        qs = City.objects.filter(city__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("city is already created")
        return value
