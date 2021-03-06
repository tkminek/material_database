import django_filters
from .models import Material, Hose, WaterContent, Temperature, FibreOrientation, RubberTemp


class HoseFilter(django_filters.FilterSet):

    HOSE_CHOICES = (
        (" Conti ", " Conti "),
        (" Maflow ", " Maflow "),
        (" Others ", " Others "),
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


class WaterFilter(django_filters.FilterSet):

    class Meta:
        model = WaterContent
        fields = {
            "name": [ "icontains" ],
        }


class TempFilter(django_filters.FilterSet):

    class Meta:
        model = Temperature
        fields = {
            "name": [ "icontains" ],
        }


class FibreFilter(django_filters.FilterSet):

    class Meta:
        model = FibreOrientation
        fields = {
            "name": [ "icontains" ],
        }


class RubberTempFilter(django_filters.FilterSet):

    class Meta:
        model = RubberTemp
        fields = {
            "name": [ "icontains" ],
        }

