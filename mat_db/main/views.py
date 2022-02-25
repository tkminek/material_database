from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import MaterialType, Material, SnCurve, EnCurve, CyclicCurve, StaticCurve, Hose, HoseDynamic, HoseStatic
from .forms import MaterialForm, HoseForm
from itertools import chain
from .apps import Graph
from . filters import MaterialFilter


def home(response):
    return render(response, "main/home.html", {})


def material_type_list(response):
    mat_type_ls = MaterialType.objects.all()
    count_ls = {}
    for mat_type in mat_type_ls:
        mat_id = mat_type.id
        count_ls[mat_type] = Material.objects.filter(material_type_id=mat_id).count()
        if Material.objects.filter(material_type_id=mat_id).count() == 0:
            count_ls[mat_type] = Hose.objects.filter(material_type_id=mat_id).count()
    return render(response, "main/material_type_list.html", {
                      "count_ls": count_ls,
                   })


def material_list(response, material_type_id):
    material_type = MaterialType.objects.get(pk=material_type_id)
    if len(material_type.hose_set.all()) != 0:
        hose_ls = Hose.objects.filter(material_type_id=material_type_id)
        my_filter = MaterialFilter(response.GET, queryset=hose_ls)
        hose_ls = my_filter.qs
        return render(response, "main/hose_list.html", {
            "hose_ls": hose_ls,
            "material_type": material_type,
            "my_filter": my_filter,
        })
    else:
        material_ls = Material.objects.filter(material_type_id=material_type_id)
        my_filter = MaterialFilter(response.GET, queryset=material_ls)
        material_ls = my_filter.qs
        return render(response, "main/material_list.html", {
            "material_ls": material_ls,
            "material_type": material_type,
            "my_filter": my_filter,
            })


def material_info(response, material_type_id, material_id):
    material_type = MaterialType.objects.get(pk=material_type_id)
    if len(material_type.hose_set.all()) != 0:
        hose_info = Hose.objects.get(pk=material_id)
        if HoseStatic.objects.filter(hose_id=material_id).exists():
            hose_static_info = HoseStatic.objects.get(hose_id=material_id)
        else:
            hose_static_info = ""
        if HoseDynamic.objects.filter(hose_id=material_id).exists():
            hose_dynamic_info = HoseDynamic.objects.get(hose_id=material_id)
        else:
            hose_dynamic_info =""
        return render(response, "main/hose_info.html", {
            "material_type": material_type,
            "hose_info": hose_info,
            "hose_static_info": hose_static_info,
            "hose_dynamic_info": hose_dynamic_info,
        })
    else:
        material_info = Material.objects.get(pk=material_id)
        c_curve=CyclicCurve.objects.filter(material_id=material_id)
        en_curve = EnCurve.objects.filter(material_id=material_id)
        sn_curve = SnCurve.objects.filter(material_id=material_id)
        s_curve = StaticCurve.objects.filter(material_id=material_id)
        curve_ls = list(chain(c_curve, en_curve, sn_curve, s_curve))
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
        data=Graph().cyclic_curve(curve_info, Material.objects.get(pk=material_id).E)
        return render(response, "main/cyclic_curve.html", {
            "material_type": material_type,
            "curve_info": curve_info,
            "material_info": material_info,
            "data": data,
        })
    elif EnCurve.objects.filter(name=curve_name).exists():
        curve_info = EnCurve.objects.get(material_id=material_id)
        data = Graph().en_curve(curve_info, Material.objects.get(pk=material_id).E)
        return render(response, "main/en_curve.html", {
            "material_type": material_type,
            "curve_info": curve_info,
            "material_info": material_info,
            "data": data,
        })
    elif SnCurve.objects.filter(name=curve_name).exists():
        curve_info = SnCurve.objects.get(material_id=material_id)
        data = Graph().sn_curve(curve_info)
        return render(response, "main/sn_curve.html", {
            "material_type": material_type,
            "curve_info": curve_info,
            "material_info": material_info,
            "data": data,
        })
    elif StaticCurve.objects.filter(name=curve_name).exists():
        curve_info = StaticCurve.objects.get(material_id=material_id)
        data = Graph().static_curve(curve_info, Material.objects.get(pk=material_id).E)
        return render(response, "main/static_curve.html", {
            "material_type": material_type,
            "curve_info": curve_info,
            "material_info": material_info,
            "data": data,
        })
    else:
        return HttpResponse("chyba")


###   CREATE/ADD/EDIT MATERIAL   ###
def create_material(response, material_type_id):
    form = MaterialForm()
    if response.method == "POST":
        form = MaterialForm(response.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data["material_type_id"] = MaterialType.objects.get(pk=material_type_id)
            model = Material(**cleaned_data)
            model.save()
            return redirect('/material_type_list/%s' % material_type_id)
    context = {"form": form, "material_type_id": material_type_id}
    return render(response, "main/add_update_form.html", context)


def update_material(response, material_type_id, material_id):
    material_info = Material.objects.get(pk=material_id)
    form = MaterialForm(instance=material_info)
    if response.method == "POST":
        form = MaterialForm(response.POST, instance=material_info)
        if form.is_valid():
            form.save()
            return redirect('/material_type_list/%s' % material_type_id)
    context = {"form": form, "material_type_id": material_type_id}
    return render(response, "main/add_update_form.html", context)


def delete_material(response, material_type_id, material_id):
    material_info = Material.objects.get(pk=material_id)
    if response.method == "POST":
        material_info.delete()
        return redirect('/material_type_list/%s' % material_type_id)
    context = {"material_type_id":material_type_id, "material_info":material_info}
    return render(response, "main/delete_form.html", context)


###   CREATE/ADD/EDIT HOSE   ###
def create_hose(response, material_type_id):
    form = HoseForm()
    if response.method == "POST":
        form = HoseForm(response.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data["material_type_id"] = MaterialType.objects.get(pk=material_type_id)
            #basic properties#
            hose_keys = ["name", "type", "material_type_id"]
            hose_dict = {x: cleaned_data[x] for x in cleaned_data if x in hose_keys}
            hose_model = Hose(**hose_dict)
            hose_model.save()
            cleaned_data["hose_id"] = Hose.objects.get(pk=hose_model.id)

            #static properties#
            static_keys = ["s_E_min40", "s_E_plus23", "s_E_plus100", "s_nu_min40", "s_nu_plus23", "s_nu_plus100", "s_comment", "hose_id"]
            static_dict = {x: cleaned_data[x] for x in cleaned_data if x in static_keys}
            static_dict_new={}
            static_dict_new["E_min40"]=static_dict["s_E_min40"]
            static_dict_new["E_plus23"] = static_dict["s_E_plus23"]
            static_dict_new["E_plus100"] = static_dict["s_E_plus100"]
            static_dict_new["nu_min40"]=static_dict["s_nu_min40"]
            static_dict_new["nu_plus23"] = static_dict["s_nu_plus23"]
            static_dict_new["nu_plus100"] = static_dict["s_nu_plus100"]
            static_dict_new["comment"] = static_dict["s_comment"]
            static_dict_new["hose_id"] = static_dict["hose_id"]
            static_model = HoseStatic(**static_dict_new)
            static_model.save()

            #dynamic properties#
            dynamic_keys = ["d_E_min40", "d_E_plus23", "d_E_plus100", "d_nu_min40", "d_nu_plus23", "d_nu_plus100", "d_comment", "hose_id"]
            dynamic_dict = {x: cleaned_data[x] for x in cleaned_data if x in dynamic_keys}
            dynamic_dict_new={}
            dynamic_dict_new["E_min40"]=dynamic_dict["d_E_min40"]
            dynamic_dict_new["E_plus23"] = dynamic_dict["d_E_plus23"]
            dynamic_dict_new["E_plus100"] = dynamic_dict["d_E_plus100"]
            dynamic_dict_new["nu_min40"]=dynamic_dict["d_nu_min40"]
            dynamic_dict_new["nu_plus23"] = dynamic_dict["d_nu_plus23"]
            dynamic_dict_new["nu_plus100"] = dynamic_dict["d_nu_plus100"]
            dynamic_dict_new["comment"] = dynamic_dict["d_comment"]
            dynamic_dict_new["hose_id"] = dynamic_dict["hose_id"]
            dynamic_model = HoseDynamic(**dynamic_dict_new)
            dynamic_model.save()

            return redirect('/material_type_list/%s' % material_type_id)
    context = {"form": form, "material_type_id": material_type_id}
    return render(response, "main/add_update_form.html", context)


