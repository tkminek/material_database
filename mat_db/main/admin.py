from django.contrib import admin
from .models import MaterialType, Material, SnCurve, EnCurve, CyclicCurve, StaticCurve
# Register your models here.
admin.site.register(MaterialType)
admin.site.register(Material)
admin.site.register(SnCurve)
admin.site.register(EnCurve)
admin.site.register(CyclicCurve)
admin.site.register(StaticCurve)
