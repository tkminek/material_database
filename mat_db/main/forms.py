from django.forms import ModelForm
from .models import MaterialType, Material, SnCurve, EnCurve, CyclicCurve, StaticCurve, Hose, HoseDynamic, HoseStatic


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        exclude = ['material_type_id']


