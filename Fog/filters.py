import django_filters
import Fog.models
from django.db.models import Q

class Game(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='price', label='Цена от и до')
    is_alpha = django_filters.BooleanFilter(method='filter_is_alpha', label='В альфа версии')
    term = django_filters.CharFilter(method='filter_term', label='')
    publisher = django_filters.CharFilter(field_name='publisher__name', label='Издатель')


    class Meta:
        model = Fog.models.Game
        fields = ['price_range', 'is_alpha', 'term', 'publisher']

    def filter_is_alpha(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(is_alpha=True)
        return queryset.filter(is_alpha=False)

    def filter_term(self, queryset, name, value):
        criteria = Q()
        for term in value.split():
            criteria &= Q(title__icontains=term) | Q(description__icontains=term)
        return queryset.filter(criteria).distinct()