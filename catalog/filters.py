import django_filters
from .models import Application


class ApplicationFilter(django_filters.FilterSet):
    class Meta:
        model = Application
        fields = ('status',)
