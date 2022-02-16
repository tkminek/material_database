from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import MaterialType, Material, SnCurve, EnCurve, CyclicCurve
from itertools import chain

def home(response):
    return render(response, "main/home.html", {})


def material_type_list(response):
    mat_type_ls = MaterialType.objects.all()
    return render(response, "main/material_type_list.html", {"mat_type_ls": mat_type_ls})


def material_list(response, material_type_id):
    material_type = MaterialType.objects.get(pk=material_type_id)
    material_ls = Material.objects.filter(material_type_id=material_type_id)
    return render(response, "main/material_list.html", {"material_ls": material_ls, "material_type": material_type})


def material_info(response, material_type_id, material_id):
    material_type = MaterialType.objects.get(pk=material_type_id)
    material_info = Material.objects.get(pk=material_id)
    c_curve=CyclicCurve.objects.filter(material_id=material_id)
    en_curve = EnCurve.objects.filter(material_id=material_id)
    sn_curve = SnCurve.objects.filter(material_id=material_id)
    curve_ls=list(chain(c_curve,en_curve,sn_curve))
    return render(response, "main/material_info.html", {
        "material_type": material_type,
        "material_info": material_info,
        "curve_ls": curve_ls,
    })


def curve_info(response, material_type_id, material_id, curve_name):
    material_type = MaterialType.objects.get(pk=material_type_id)
    material_info = Material.objects.get(pk=material_id)
    if CyclicCurve.objects.filter(name=curve_name).exists():
        curve_info = CyclicCurve.objects.get(material_id=material_id)
        return render(response, "main/cyclic_curve.html", {
            "material_type": material_type,
            "curve_info": curve_info,
            "material_info": material_info,
        })
    elif EnCurve.objects.filter(name=curve_name).exists():
        curve_info = EnCurve.objects.get(material_id=material_id)
        return render(response, "main/en_curve.html", {
            "material_type": material_type,
            "curve_info": curve_info,
            "material_info": material_info,
        })
    elif SnCurve.objects.filter(name=curve_name).exists():
        curve_info = SnCurve.objects.get(material_id=material_id)
        return render(response, "main/sn_curve.html", {
            "material_type": material_type,
            "curve_info": curve_info,
            "material_info": material_info,
        })
    else:
        return HttpResponse("chyba")