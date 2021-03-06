from .models import MaterialType, Material, SnCurve, EnCurve, CyclicCurve, StaticCurve, Hose, HoseDynamic, HoseStatic, Plastic, WaterContent, Temperature, FibreOrientation, FibreStaticCurve, FibreSnCurve, Rubber, RubberTemp, ArrudaBoyce, MooneyRivlin, Polynomial, Yeoh, Ogden, NeoHooke, MaterialCustomCurve, PlasticCustomCurve, RubberCustomCurve
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
            "Sa": forms.TextInput(attrs={"class": "form-control", "placeholder": 'Strain Amplitude List - Split By ","'}),
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
            "Sa": forms.TextInput(attrs={"class": "form-control", "placeholder": 'Strain Amplitude List - Split By ","'}),
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
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Material Name"}),
            "E": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Young's Modulus"}),
            "nu": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Poisson's Ratio"}),
            "rho": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Density"}),
            "Rm": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Ultimate Tensile Strength"}),
            "Re": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Yield Stress"}),
            "Ru": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Fatigue Limit"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments"}),
        }


class ArrudaBoyceForm(forms.ModelForm):
    class Meta:
        model = ArrudaBoyce
        exclude = ['rubber_temp_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Model Name"}),
            "nu": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type μ Value"}),
            "lambda_m": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type λm Value"}),
            "D": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type D Value"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments"}),
        }


class MooneyRivlinForm(forms.ModelForm):
    class Meta:
        model = MooneyRivlin
        exclude = ['rubber_temp_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Model Name"}),
            "C_10": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type C_10 Value"}),
            "C_01": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type C_01 Value"}),
            "D_1": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type D_1 Value"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments"}),
        }


class PolynomialForm(forms.ModelForm):
    class Meta:
        model = Polynomial
        exclude = ['rubber_temp_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Model Name"}),
            "C_10": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type C_10 Value"}),
            "C_20": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type C_20 Value"}),
            "C_30": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type C_30 Value"}),
            "D_1": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type D_1 Value"}),
            "D_2": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type D_2 Value"}),
            "D_3": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type D_3 Value"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments"}),
        }


class YeohForm(forms.ModelForm):
    class Meta:
        model = Yeoh
        exclude = ['rubber_temp_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Model Name"}),
            "C_10": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type C_10 Value"}),
            "C_20": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type C_20 Value"}),
            "C_30": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type C_30 Value"}),
            "D_1": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type D_1 Value"}),
            "D_2": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type D_2 Value"}),
            "D_3": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type D_3 Value"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments"}),
        }


class OgdenForm(forms.ModelForm):
    class Meta:
        model = Ogden
        exclude = ['rubber_temp_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Model Name"}),
            "nu_1": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type μ1 Value"}),
            "alfa_1": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type α1 Value"}),
            "D_1": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type D1 Value"}),
            "nu_2": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type μ2 Value"}),
            "alfa_2": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type α2 Value"}),
            "D_2": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type D2 Value"}),
            "nu_3": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type μ3 Value"}),
            "alfa_3": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type α3 Value"}),
            "D_3": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type D3 Value"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments"}),
        }


class NeoHookeForm(forms.ModelForm):
    class Meta:
        model = NeoHooke
        exclude = ['rubber_temp_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Model Name"}),
            "C_10": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type C_10 Value"}),
            "D_1": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type D_1 Value"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments"}),
        }


class MaterialCustomCurveForm(forms.ModelForm):
    class Meta:
        model = MaterialCustomCurve
        exclude = ['material_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Cyclic Curve Name"}),
            "curve_type": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Curve Type"}),
            "x_axis": forms.TextInput(attrs={"class": "form-control", "placeholder": 'Type X Axis Name And unit'}),
            "x_axis_type": forms.Select(attrs={"class": "form-control", "placeholder": 'Choice X Axis Type'}),
            "x_value": forms.TextInput(attrs={"class": "form-control", "placeholder": 'X Axis Value List - Split By ","'}),
            "y_axis": forms.TextInput(attrs={"class": "form-control", "placeholder": 'Type Y Axis Name And Unit'}),
            "y_axis_type": forms.Select(attrs={"class": "form-control", "placeholder": 'Choice Y Axis Type'}),
            "y_value": forms.TextInput(attrs={"class": "form-control", "placeholder": 'Y Axis Value List - Split By ","'}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type Your Comments For Curve"}),
        }


class PlasticCustomCurveForm(forms.ModelForm):
    class Meta:
        model = PlasticCustomCurve
        exclude = ['fibre_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Cyclic Curve Name"}),
            "curve_type": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Curve Type"}),
            "x_axis": forms.TextInput(
                attrs={"class": "form-control", "placeholder": 'Type X Axis Name And unit'}),
            "x_axis_type": forms.Select(attrs={"class": "form-control", "placeholder": 'Choice X Axis Type'}),
            "x_value": forms.TextInput(
                attrs={"class": "form-control", "placeholder": 'X Axis Value List - Split By ","'}),
            "y_axis": forms.TextInput(
                attrs={"class": "form-control", "placeholder": 'Type Y Axis Name And Unit'}),
            "y_axis_type": forms.Select(attrs={"class": "form-control", "placeholder": 'Choice Y Axis Type'}),
            "y_value": forms.TextInput(
                attrs={"class": "form-control", "placeholder": 'Y Axis Value List - Split By ","'}),
            "comment": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Type Your Comments For Curve"}),
        }


class RubberCustomCurveForm(forms.ModelForm):
    class Meta:
        model = RubberCustomCurve
        exclude = ['rubber_temp_id']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Cyclic Curve Name"}),
            "curve_type": forms.TextInput(attrs={"class": "form-control", "placeholder": "Type Curve Type"}),
            "x_axis": forms.TextInput(
                attrs={"class": "form-control", "placeholder": 'Type X Axis Name And unit'}),
            "x_axis_type": forms.Select(attrs={"class": "form-control", "placeholder": 'Choice X Axis Type'}),
            "x_value": forms.TextInput(
                attrs={"class": "form-control", "placeholder": 'X Axis Value List - Split By ","'}),
            "y_axis": forms.TextInput(
                attrs={"class": "form-control", "placeholder": 'Type Y Axis Name And Unit'}),
            "y_axis_type": forms.Select(attrs={"class": "form-control", "placeholder": 'Choice Y Axis Type'}),
            "y_value": forms.TextInput(
                attrs={"class": "form-control", "placeholder": 'Y Axis Value List - Split By ","'}),
            "comment": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Type Your Comments For Curve"}),
        }