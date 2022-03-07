from django.db import models


class MaterialType(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=200, unique=True)
    E = models.FloatField()
    nu = models.FloatField()
    Rm = models.FloatField()
    Re = models.FloatField()
    Ru = models.FloatField()
    comment = models.CharField(max_length=1000)
    material_type_id = models.ForeignKey(MaterialType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CyclicCurve(models.Model):
    curve_type = "Cyclic curve"
    name = models.CharField(max_length=200, unique=True)
    K = models.FloatField(max_length=200)
    n = models.FloatField(max_length=200)
    comment = models.CharField(max_length=1000)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StaticCurve(models.Model):
    curve_type = "Static curve"
    name = models.CharField(max_length=200, unique=True)
    K = models.FloatField(max_length=200)
    n = models.FloatField(max_length=200)
    comment = models.CharField(max_length=1000)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class EnCurve(models.Model):
    curve_type = "En curve"
    name = models.CharField(max_length=200, unique=True)
    Sf = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    Ef = models.FloatField()
    comment = models.CharField(max_length=1000)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SnCurve(models.Model):
    curve_type = "Sn curve"
    name = models.CharField(max_length=200, unique=True)
    Sa = models.CharField(max_length=20000)
    Nf = models.CharField(max_length=20000)
    comment = models.CharField(max_length=1000)
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
    Stat_E_min40 = models.FloatField()
    Stat_E_plus23 = models.FloatField()
    Stat_E_plus100 = models.FloatField()
    Stat_nu_min40 = models.FloatField(default=0.495)
    Stat_nu_plus23 = models.FloatField(default=0.495)
    Stat_nu_plus100 = models.FloatField(default=0.495)
    Stat_comment = models.CharField(max_length=1000)
    Stat_hose_id = models.ForeignKey(Hose, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class HoseDynamic(models.Model):
    Dyn_E_min40 = models.FloatField()
    Dyn_E_plus23 = models.FloatField()
    Dyn_E_plus100 = models.FloatField()
    Dyn_nu_min40 = models.FloatField(default=0.495)
    Dyn_nu_plus23 = models.FloatField(default=0.495)
    Dyn_nu_plus100 = models.FloatField(default=0.495)
    Dyn_comment = models.CharField(max_length=1000)
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
    E = models.FloatField()
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
    K = models.FloatField(max_length=200)
    n = models.FloatField(max_length=200)
    comment = models.CharField(max_length=1000)
    fibre_id = models.ForeignKey(FibreOrientation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FibreSnCurve(models.Model):
    curve_type = "Sn curve"
    name = models.CharField(max_length=200, unique=True)
    Sa = models.CharField(max_length=20000)
    Nf = models.CharField(max_length=20000)
    comment = models.CharField(max_length=1000)
    fibre_id = models.ForeignKey(FibreOrientation, on_delete=models.CASCADE)


class Rubber(models.Model):
    name = models.CharField(max_length=200, unique=True)
    material_type_id = models.ForeignKey(MaterialType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RubberTemp(models.Model):
    name = models.CharField(max_length=200)
    rubber_id = models.ForeignKey(Rubber, on_delete=models.CASCADE)
    E = models.FloatField()
    nu = models.FloatField(blank=True)
    rho = models.FloatField(blank=True)
    Rm = models.FloatField(blank=True)
    Re = models.FloatField(blank=True)
    Ru = models.FloatField(blank=True)
    comment = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name

