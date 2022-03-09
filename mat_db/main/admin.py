from django.contrib import admin
from .models import MaterialType, Material, SnCurve, EnCurve, CyclicCurve, StaticCurve, Hose, HoseStatic, HoseDynamic, Plastic,  WaterContent, Temperature, FibreOrientation, FibreStaticCurve, FibreSnCurve, Rubber, RubberTemp, ArrudaBoyce, PlasticCustomCurve, MaterialCustomCurve, RubberCustomCurve
# Register your models here.
admin.site.register(MaterialType)
admin.site.register(Material)
admin.site.register(SnCurve)
admin.site.register(EnCurve)
admin.site.register(CyclicCurve)
admin.site.register(StaticCurve)
admin.site.register(Hose)
admin.site.register(HoseStatic)
admin.site.register(HoseDynamic)
admin.site.register(Plastic)
admin.site.register(WaterContent)
admin.site.register(Temperature)
admin.site.register(FibreOrientation)
admin.site.register(FibreSnCurve)
admin.site.register(FibreStaticCurve)
admin.site.register(Rubber)
admin.site.register(RubberTemp)
admin.site.register(ArrudaBoyce)
admin.site.register(MaterialCustomCurve)
admin.site.register(PlasticCustomCurve)
admin.site.register(RubberCustomCurve)








