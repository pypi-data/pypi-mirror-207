"""Filters for dictionaries."""

from django.db.models import Q, QuerySet
from django_filters.filters import CharFilter
from django_filters.filterset import FilterSet

from .models import Organization


class OrganizationFilter(FilterSet):
    """Organization filter."""

    id__icontains = CharFilter(field_name='id', lookup_expr='icontains')
    attributes = CharFilter(field_name='attributes', lookup_expr='level__exact')

    class Meta:
        model = Organization
        fields = {
            'id': ('exact', 'in',),
            'parent': ('exact', 'isnull'),
            'name': ('exact', 'icontains',),
            'inn': ('exact', 'icontains',),
            'kpp': ('exact', 'icontains',),
            'kind': ('exact', 'icontains',),
            'rubpnubp': ('exact', 'icontains',),
            'kodbuhg': ('exact', 'icontains',),
            'okpo': ('exact', 'icontains',),
            'phone': ('exact', 'icontains',),
            'site': ('exact', 'icontains',),
            'mail': ('exact', 'icontains',),
            'address': ('exact', 'icontains',),
            'region': ('exact', 'in',),
            'department': ('exact', 'in',)
        }

    @property
    def qs(self) -> QuerySet:
        """Filter with `or` for `icontains` lookup and with `and` for the rest."""
        queryset = self.queryset
        search_q = Q()
        for field, value in self.data.items():
            if 'icontains' in field:
                search_q |= Q(**{field: value})
            else:
                queryset = queryset.filter(**{field: value})
        return queryset.filter(search_q)
