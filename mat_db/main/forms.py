from django.forms import ModelForm
from .models import MaterialType, Material, SnCurve, EnCurve, CyclicCurve, StaticCurve, Hose, HoseDynamic, HoseStatic



class MaterialForm(ModelForm):
    class Meta:
        model = Material
        exclude = ['material_type_id']


class HoseForm(ModelForm):
    class Meta:
        model = Hose
        exclude = ['material_type_id']


class HoseStaticForm(ModelForm):
    class Meta:
        model = HoseStatic
        exclude = ['Stat_hose_id', 'Stat_name']


class HoseDynamicForm(ModelForm):
    class Meta:
        model = HoseDynamic
        exclude = ['Dyn_hose_id', 'Dyn_name']



