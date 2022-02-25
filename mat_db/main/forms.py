from django.forms import ModelForm
from .models import MaterialType, Material, SnCurve, EnCurve, CyclicCurve, StaticCurve, Hose, HoseDynamic, HoseStatic
from django import forms

class MaterialForm(ModelForm):
    class Meta:
        model = Material
        exclude = ['material_type_id']


class HoseForm(forms.Form):
    name = forms.CharField(label="Name")
    type = forms.CharField(label="Type")
    s_E_min40 = forms.FloatField(label="s_E_min40")
    s_E_plus23 = forms.FloatField(label="s_E_plus23")
    s_E_plus100 = forms.FloatField(label="s_E_plus100")
    s_nu_min40 = forms.FloatField(label="s_nu_min40")
    s_nu_plus23 = forms.FloatField(label="s_nu_plus23")
    s_nu_plus100 = forms.FloatField(label="s_nu_plus100")
    s_comment = forms.CharField(label="s_comment")
    d_E_min40 = forms.FloatField(label="d_E_min40")
    d_E_plus23 = forms.FloatField(label="d_E_plus23")
    d_E_plus100 = forms.FloatField(label="d_E_plus100")
    d_nu_min40 = forms.FloatField(label="d_nu_min40")
    d_nu_plus23 = forms.FloatField(label="d_nu_plus23")
    d_nu_plus100 = forms.FloatField(label="d_nu_plus100")
    d_comment = forms.CharField(label="d_comment")
