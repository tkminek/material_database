from django.db import models


class MaterialType(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=200, unique=True)
    E = models.FloatField(blank=True)
    nu = models.FloatField(blank=True)
    Rm = models.FloatField(blank=True)
    Re = models.FloatField(blank=True)
    Ru = models.FloatField(blank=True)
    comment = models.CharField(blank=True, max_length=1000)
    material_type_id = models.ForeignKey(MaterialType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CyclicCurve(models.Model):
    curve_type = "Cyclic curve"
    name = models.CharField(max_length=200, unique=True)
    K = models.FloatField(max_length=200, blank=True)
    n = models.FloatField(max_length=200, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StaticCurve(models.Model):
    curve_type = "Static curve"
    name = models.CharField(max_length=200, unique=True)
    K = models.FloatField(max_length=200, blank=True)
    n = models.FloatField(max_length=200, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class EnCurve(models.Model):
    curve_type = "En curve"
    name = models.CharField(max_length=200, unique=True)
    Sf = models.FloatField(blank=True)
    b = models.FloatField(blank=True)
    c = models.FloatField(blank=True)
    Ef = models.FloatField(blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SnCurve(models.Model):
    curve_type = "Sn curve"
    name = models.CharField(max_length=200, unique=True)
    Sa = models.CharField(max_length=20000, blank=True)
    Nf = models.CharField(max_length=20000, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


HOSE_CHOICES = (
    (" Conti ", " Conti "),
    (" Maflow ", " Maflow "),
)


class Hose(models.Model):
    name = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=200, choices=HOSE_CHOICES)
    material_type_id = models.ForeignKey(MaterialType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class HoseStatic(models.Model):
    Stat_E_min40 = models.FloatField(blank=True)
    Stat_E_plus23 = models.FloatField(blank=True)
    Stat_E_plus100 = models.FloatField(blank=True)
    Stat_nu_min40 = models.FloatField(default=0.495, blank=True)
    Stat_nu_plus23 = models.FloatField(default=0.495, blank=True)
    Stat_nu_plus100 = models.FloatField(default=0.495, blank=True)
    Stat_comment = models.CharField(max_length=1000, blank=True)
    Stat_hose_id = models.ForeignKey(Hose, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class HoseDynamic(models.Model):
    Dyn_E_min40 = models.FloatField(blank=True)
    Dyn_E_plus23 = models.FloatField(blank=True)
    Dyn_E_plus100 = models.FloatField(blank=True)
    Dyn_nu_min40 = models.FloatField(default=0.495, blank=True)
    Dyn_nu_plus23 = models.FloatField(default=0.495, blank=True)
    Dyn_nu_plus100 = models.FloatField(default=0.495, blank=True)
    Dyn_comment = models.CharField(max_length=1000, blank=True)
    Dyn_hose_id = models.ForeignKey(Hose, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Plastic(models.Model):
    name = models.CharField(max_length=200, unique=True)
    material_type_id = models.ForeignKey(MaterialType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WaterContent(models.Model):
    name = models.CharField(max_length=200)
    plastic_id = models.ForeignKey(Plastic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Temperature(models.Model):
    name = models.CharField(max_length=200)
    water_content_id = models.ForeignKey(WaterContent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FibreOrientation(models.Model):
    name = models.CharField(max_length=200)
    E = models.FloatField(blank=True)
    nu = models.FloatField(blank=True)
    rho = models.FloatField(blank=True)
    Rm = models.FloatField(blank=True)
    Re = models.FloatField(blank=True)
    Ru = models.FloatField(blank=True)
    comment = models.CharField(max_length=1000, default="")
    temperature_id = models.ForeignKey(Temperature, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FibreStaticCurve(models.Model):
    curve_type = "Static curve"
    name = models.CharField(max_length=200, unique=True)
    K = models.FloatField(max_length=200, blank=True)
    n = models.FloatField(max_length=200, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    fibre_id = models.ForeignKey(FibreOrientation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FibreSnCurve(models.Model):
    curve_type = "Sn curve"
    name = models.CharField(max_length=200, unique=True)
    Sa = models.CharField(max_length=20000, blank=True)
    Nf = models.CharField(max_length=20000, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    fibre_id = models.ForeignKey(FibreOrientation, on_delete=models.CASCADE)


class Rubber(models.Model):
    name = models.CharField(max_length=200, unique=True)
    material_type_id = models.ForeignKey(MaterialType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RubberTemp(models.Model):
    name = models.CharField(max_length=200, unique=True)
    rubber_id = models.ForeignKey(Rubber, on_delete=models.CASCADE)
    E = models.FloatField(blank=True)
    nu = models.FloatField(blank=True)
    rho = models.FloatField(blank=True)
    Rm = models.FloatField(blank=True)
    Re = models.FloatField(blank=True)
    Ru = models.FloatField(blank=True)
    comment = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


class ArrudaBoyce(models.Model):
    model_type = "Arruda-Boyce"
    name = models.CharField(max_length=200, unique=True)
    nu = models.CharField(max_length=20000, blank=True)
    lambda_m = models.CharField(max_length=20000, blank=True)
    D = models.CharField(max_length=20000, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    rubber_temp_id = models.ForeignKey(RubberTemp, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MooneyRivlin(models.Model):
    model_type = "Mooney-Rivlin"
    name = models.CharField(max_length=200, unique=True)
    C_10 = models.CharField(max_length=20000, blank=True)
    C_01 = models.CharField(max_length=20000, blank=True)
    D_1 = models.CharField(max_length=20000, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    rubber_temp_id = models.ForeignKey(RubberTemp, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Polynomial(models.Model):
    model_type = "Polynomial"
    name = models.CharField(max_length=200, unique=True)
    C_10 = models.CharField(max_length=20000, blank=True)
    C_20 = models.CharField(max_length=20000, blank=True)
    C_30 = models.CharField(max_length=20000, blank=True)
    D_1 = models.CharField(max_length=20000, blank=True)
    D_2 = models.CharField(max_length=20000, blank=True)
    D_3 = models.CharField(max_length=20000, blank=True)
    comment = models.CharField(max_length=1000)
    rubber_temp_id = models.ForeignKey(RubberTemp, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Yeoh(models.Model):
    model_type = "Yeoh"
    name = models.CharField(max_length=200, unique=True)
    C_10 = models.CharField(max_length=20000, blank=True)
    C_20 = models.CharField(max_length=20000, blank=True)
    C_30 = models.CharField(max_length=20000, blank=True)
    D_1 = models.CharField(max_length=20000, blank=True)
    D_2 = models.CharField(max_length=20000, blank=True)
    D_3 = models.CharField(max_length=20000, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    rubber_temp_id = models.ForeignKey(RubberTemp, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ogden(models.Model):
    model_type = "Ogden"
    name = models.CharField(max_length=200, unique=True)
    nu_1 = models.CharField(max_length=20000, blank=True)
    alfa_1 = models.CharField(max_length=20000, blank=True)
    D_1 = models.CharField(max_length=20000, blank=True)
    nu_2 = models.CharField(max_length=20000, blank=True)
    alfa_2 = models.CharField(max_length=20000, blank=True)
    D_2 = models.CharField(max_length=20000, blank=True)
    nu_3 = models.CharField(max_length=20000, blank=True)
    alfa_3 = models.CharField(max_length=20000, blank=True)
    D_3 = models.CharField(max_length=20000, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    rubber_temp_id = models.ForeignKey(RubberTemp, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class NeoHooke(models.Model):
    model_type = "Neo-Hooke"
    name = models.CharField(max_length=200, unique=True)
    C_10 = models.CharField(max_length=20000, blank=True)
    D_1 = models.CharField(max_length=20000, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    rubber_temp_id = models.ForeignKey(RubberTemp, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MaterialCustomCurve(models.Model):
    name = models.CharField(max_length=200, unique=True)
    curve_type = models.CharField(max_length=20000, blank=True)
    x_axis = models.CharField(max_length=20000, blank=True)
    x_axis_type = models.CharField(max_length=200, choices=(("lin", "lin"), ("log", "log")))
    x_value = models.CharField(max_length=20000, blank=True)
    y_axis = models.CharField(max_length=20000, blank=True)
    y_axis_type = models.CharField(max_length=200, choices=(("lin", "lin"), ("log", "log")))
    y_value = models.CharField(max_length=20000, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)


class PlasticCustomCurve(models.Model):
    name = models.CharField(max_length=200, unique=True)
    curve_type = models.CharField(max_length=20000, blank=True)
    x_axis = models.CharField(max_length=20000, blank=True)
    x_axis_type = models.CharField(max_length=200, choices=(("lin", "lin"), ("log", "log")))
    x_value = models.CharField(max_length=20000, blank=True)
    y_axis = models.CharField(max_length=20000, blank=True)
    y_axis_type = models.CharField(max_length=200, choices=(("lin", "lin"), ("log", "log")))
    y_value = models.CharField(max_length=20000, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    fibre_id = models.ForeignKey(FibreOrientation, on_delete=models.CASCADE)


class RubberCustomCurve(models.Model):
    name = models.CharField(max_length=200, unique=True)
    curve_type = models.CharField(max_length=20000, blank=True)
    x_axis = models.CharField(max_length=20000, blank=True)
    x_axis_type = models.CharField(max_length=200, choices=(("lin", "lin"), ("log", "log")))
    x_value = models.CharField(max_length=20000, blank=True)
    y_axis = models.CharField(max_length=20000, blank=True)
    y_axis_type = models.CharField(max_length=200, choices=(("lin", "lin"), ("log", "log")))
    y_value = models.CharField(max_length=20000, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    rubber_temp_id = models.ForeignKey(RubberTemp, on_delete=models.CASCADE)