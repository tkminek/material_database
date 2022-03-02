import django_filters
from .models import Material, Hose


class HoseFilter(django_filters.FilterSet):

    HOSE_CHOICES = (
        ("GOODYER", "Goodyer"),
        ("ARCTIC NK", "Arctic NK"),
    )

    type = django_filters.ChoiceFilter(label="Hose type",choices=HOSE_CHOICES)

    class Meta:
        model = Hose
        fields = {
            "name": [ "icontains" ],
        }

class MaterialFilter(django_filters.FilterSet):

    class Meta:
        model = Material
        fields = {
            "name": [ "icontains" ],
        }

