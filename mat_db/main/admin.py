from django.contrib import admin
from .models import MaterialType, Material, SnCurve, EnCurve, CyclicCurve, StaticCurve, Hose, HoseStatic, HoseDynamic
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
