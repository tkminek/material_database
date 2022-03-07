from .models import MaterialType, Material, SnCurve, EnCurve, CyclicCurve, StaticCurve, Hose, HoseDynamic, HoseStatic, Plastic, WaterContent, Temperature, FibreOrientation, FibreStaticCurve, FibreSnCurve, Rubber, RubberTemp
from django import forms


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        exclude = ['material_type_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Material Name"}),
            "E": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Young's Modulus"}),
            "nu": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Poisson's Ratio"}),
            "Rm": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Ultimate Tensile Strength"}),
            "Re": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Yield Stress"}),
            "Ru": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Fatigue Limit"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments"}),
        }


class HoseForm(forms.ModelForm):
    class Meta:
        model = Hose
        exclude = ['material_type_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Material Name"}),
            "type": forms.Select(attrs={"class": "form-control", "placeholder": "Choice Type Of Hose"}),
        }


class HoseStaticForm(forms.ModelForm):
    class Meta:
        model = HoseStatic
        exclude = ['Stat_hose_id', 'Stat_name']
        widgets = {
            "Stat_E_min40": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Young's Modulus for -40 °C"}),
            "Stat_E_plus23": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Young's Modulus for 23 °C"}),
            "Stat_E_plus100": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Young's Modulus for 100 °C"}),
            "Stat_nu_min40": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Poisson's Ratio for -40 °C"}),
            "Stat_nu_plus23": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Poisson's Ratio for -23 °C"}),
            "Stat_nu_plus100": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Poisson's Ratio for 100 °C"}),
            "Stat_comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments For Static Behaviour."}),
        }


class HoseDynamicForm(forms.ModelForm):
    class Meta:
        model = HoseDynamic
        exclude = ['Dyn_hose_id', 'Dyn_name']
        widgets = {
            "Dyn_E_min40": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Young's Modulus for -40 °C"}),
            "Dyn_E_plus23": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Young's Modulus for 23 °C"}),
            "Dyn_E_plus100": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Young's Modulus for 100 °C"}),
            "Dyn_nu_min40": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Poisson's Ratio for -40 °C"}),
            "Dyn_nu_plus23": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Poisson's Ratio for -23 °C"}),
            "Dyn_nu_plus100": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Poisson's Ratio for 100 °C"}),
            "Dyn_comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments For Dynamic Behaviour."}),
        }


class CyclicCurveForm(forms.ModelForm):
    class Meta:
        model = CyclicCurve
        exclude = ['material_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Cyclic Curve Name"}),
            "K": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Cyclic Strain Hardening Coefficient"}),
            "n": forms.TextInput(attrs={"class": "form-control", "placeholder": "Cyclic Strain Hardening Exponent"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments For Cylic Curve"}),
        }


class StaticCurveForm(forms.ModelForm):
    class Meta:
        model = StaticCurve
        exclude = ['material_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Cyclic Curve Name"}),
            "K": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Static Strain Hardening Coefficient"}),
            "n": forms.TextInput(attrs={"class": "form-control", "placeholder": "Cyclic Static Hardening Exponent"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments For Static Curve"}),
        }


class EnCurveForm(forms.ModelForm):
    class Meta:
        model = EnCurve
        exclude = ['material_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Cyclic Curve Name"}),
            "Sf": forms.TextInput(attrs={"class": "form-control", "placeholder": "Fatigue Strength Coefficient"}),
            "b": forms.TextInput(attrs={"class": "form-control", "placeholder": "Fatigue Strength Exponent"}),
            "c": forms.TextInput(attrs={"class": "form-control", "placeholder": "Fatigue Ductility Exponent"}),
            "Ef": forms.TextInput(attrs={"class": "form-control", "placeholder": "Fatigue Ductility Coefficient"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments For En Curve"}),
        }


class SnCurveForm(forms.ModelForm):
    class Meta:
        model = SnCurve
        exclude = ['material_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Cyclic Curve Name"}),
            "Sa": forms.TextInput(attrs={"class": "form-control", "placeholder": "Strain Amplitude List"}),
            "Nf": forms.TextInput(attrs={"class": "form-control", "placeholder": 'Number Of Cycles - Split By ","'}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments For Static Curve"}),
        }


class PlasticForm(forms.ModelForm):
    class Meta:
        model = Plastic
        exclude = ['material_type_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Material Name"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments"}),
        }


class WaterContentForm(forms.ModelForm):
    class Meta:
        model = WaterContent
        exclude = ['plastic_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Humidity Name"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments"}),
        }


class TemperatureForm(forms.ModelForm):
    class Meta:
        model = Temperature
        exclude = ['water_content_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Temperature Name"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments"}),
        }


class FibreOrientationForm(forms.ModelForm):
    class Meta:
        model = FibreOrientation
        exclude = ['temperature_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Material Name"}),
            "E": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Young's Modulus"}),
            "nu": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Poisson's Ratio"}),
            "rho": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Density"}),
            "Rm": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Ultimate Tensile Strength"}),
            "Re": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Yield Stress"}),
            "Ru": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Fatigue Limit"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments"}),
        }


class FibreStaticCurveForm(forms.ModelForm):
    class Meta:
        model = FibreStaticCurve
        exclude = ['fibre_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Cyclic Curve Name"}),
            "K": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Static Strain Hardening Coefficient"}),
            "n": forms.TextInput(attrs={"class": "form-control", "placeholder": "Cyclic Static Hardening Exponent"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments For Static Curve"}),
        }


class FibreSnCurveForm(forms.ModelForm):
    class Meta:
        model = FibreSnCurve
        exclude = ['fibre_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Cyclic Curve Name"}),
            "Sa": forms.TextInput(attrs={"class": "form-control", "placeholder": "Strain Amplitude List"}),
            "Nf": forms.TextInput(attrs={"class": "form-control", "placeholder": 'Number Of Cycles - Split By ","'}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments For Static Curve"}),
        }


class RubberForm(forms.ModelForm):
    class Meta:
        model = Rubber
        exclude = ['material_type_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Material Name"}),
        }


class RubberTempForm(forms.ModelForm):
    class Meta:
        model = RubberTemp
        exclude = ['rubber_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Temperature Name"}),
        }
