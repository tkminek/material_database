from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import MaterialType, Material, SnCurve, EnCurve, CyclicCurve


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
    material_info = Material.objects.get(pk=material_id)
    return render(response, "main/material_info.html", {"material_info": material_info})