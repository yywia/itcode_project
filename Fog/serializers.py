from rest_framework import serializers
from Fog import models

class Statistics(serializers.ModelSerializer):
    class Meta:
        model = models.Statistics
        fields = '__all__'

class Genre(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'

class Developer(serializers.ModelSerializer):
    class Meta:
        model = models.Developer
        fields = '__all__'

class Publisher(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = '__all__'

class Game(serializers.ModelSerializer):
    statistics = Statistics(read_only=True)
    genre = Genre(read_only=True, many=True)
    publisher = Publisher(read_only=True)
    publisher_id = serializers.IntegerField(required=False, allow_null=True)
    developer = Developer(read_only=True)
    developer_id = serializers.IntegerField(required=False, allow_null=True)
    price = serializers.SerializerMethodField()
    class Meta:
        model = models.Game
        fields = '__all__'

    def get_price(self, obj):
        if models.Game.objects.filter(id=obj.pk).exists():
            return obj.price
        return None