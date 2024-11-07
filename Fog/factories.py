import factory
from factory.django import ImageField

from Fog import models

class PublisherFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    description = factory.Faker('text')

    class Meta:
        model = models.Publisher

class DeveloperFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    description = factory.Faker('text')

    class Meta:
        model = models.Developer

class GameFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('name')
    price = factory.Faker('pyfloat')
    description = factory.Faker('text')
    release_date = factory.Faker('date')
    image = ImageField()
    developer = factory.SubFactory(DeveloperFactory)
    publisher = factory.SubFactory(PublisherFactory)

    class Meta:
        model = models.Game

class StatisticsFactory(factory.django.DjangoModelFactory):
    review_score = factory.Faker('pyfloat')
    review_amount = factory.Faker('pyint')
    game = factory.SubFactory(GameFactory)

    class Meta:
        model = models.Statistics