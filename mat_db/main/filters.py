import django_filters
from .models import Material


class MaterialFilter(django_filters.FilterSet):

    class Meta:
        model = Material
        fields = {
            "name": [ "icontains" ],
        }