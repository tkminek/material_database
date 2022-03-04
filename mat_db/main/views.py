from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import MaterialType, Material, SnCurve, EnCurve, CyclicCurve, StaticCurve, Hose, HoseDynamic, HoseStatic, Plastic, WaterContent, Temperature, PlasticInfo
from .forms import MaterialForm, HoseForm, HoseStaticForm, HoseDynamicForm, StaticCurveForm, CyclicCurveForm, EnCurveForm, SnCurveForm
from itertools import chain
from .apps import Graph
from . filters import MaterialFilter, HoseFilter, WaterFilter, TempFilter


def home(response):
    return render(response, "main/home.html", {})


def material_type_list(response):
    mat_type_ls = MaterialType.objects.all()
    count_ls = {}
    for mat_type in mat_type_ls:
        mat_id = mat_type.id
        if Material.objects.filter(material_type_id=mat_id).count() != 0:
            count_ls[mat_type] = Material.objects.filter(material_type_id=mat_id).count()
        elif Hose.objects.filter(material_type_id=mat_id).count() != 0:
            count_ls[mat_type] = Hose.objects.filter(material_type_id=mat_id).count()
        elif Plastic.objects.filter(material_type_id=mat_id).count() != 0:
            count_ls[mat_type] = Plastic.objects.filter(material_type_id=mat_id).count()
    return render(response, "main/material_type_list.html", {
                      "count_ls": count_ls,
                   })


def material_list(response, material_type_id):
    material_type = MaterialType.objects.get(pk=material_type_id)
    if len(material_type.hose_set.all()) != 0:
        hose_ls = Hose.objects.filter(material_type_id=material_type_id)
        my_filter = HoseFilter(response.GET, queryset=hose_ls)
        hose_ls = my_filter.qs
        return render(response, "main/hose_list.html", {
            "hose_ls": hose_ls,
            "material_type": material_type,
            "my_filter": my_filter,
        })
    elif len(material_type.material_set.all()) != 0:
        material_ls = Material.objects.filter(material_type_id=material_type_id)
        my_filter = MaterialFilter(response.GET, queryset=material_ls)
        material_ls = my_filter.qs
        return render(response, "main/material_list.html", {
            "material_ls": material_ls,
            "material_type": material_type,
            "my_filter": my_filter,
            })
    elif len(material_type.plastic_set.all()) != 0:
        material_ls = Plastic.objects.filter(material_type_id=material_type_id)
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
        if HoseStatic.objects.filter(Stat_hose_id=material_id).exists():
            hose_static_info = HoseStatic.objects.get(Stat_hose_id=material_id)
        else:
            hose_static_info = ""
        if HoseDynamic.objects.filter(Dyn_hose_id=material_id).exists():
            hose_dynamic_info = HoseDynamic.objects.get(Dyn_hose_id=material_id)
        else:
            hose_dynamic_info =""
        return render(response, "main/hose_info.html", {
            "material_type": material_type,
            "hose_info": hose_info,
            "hose_static_info": hose_static_info,
            "hose_dynamic_info": hose_dynamic_info,
        })
    elif len(material_type.material_set.all()) != 0:
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
    elif len(material_type.plastic_set.all()) != 0:
        material_info = Plastic.objects.get(pk=material_id)
        water_ls = WaterContent.objects.filter(plastic_id=material_id)
        my_filter = WaterFilter(response.GET, queryset=water_ls)
        water_ls = my_filter.qs
        return render(response, "main/water_list.html", {
            "material_info": material_info,
            "material_type": material_type,
            "water_ls": water_ls,
            "my_filter": my_filter,
        })


def curve_info(response, material_type_id, material_id, curve_name):
    material_type = MaterialType.objects.get(pk=material_type_id)
    material_info = Material.objects.get(pk=material_id)
    if CyclicCurve.objects.filter(name=curve_name).exists():
        curve_info = CyclicCurve.objects.get(name=curve_name)
        data=Graph().cyclic_curve(curve_info, Material.objects.get(pk=material_id).E)
        return render(response, "main/cyclic_curve.html", {
            "material_type": material_type,
            "curve_info": curve_info,
            "material_info": material_info,
            "data": data,
        })
    elif EnCurve.objects.filter(name=curve_name).exists():
        curve_info = EnCurve.objects.get(name=curve_name)
        data = Graph().en_curve(curve_info, Material.objects.get(pk=material_id).E)
        return render(response, "main/en_curve.html", {
            "material_type": material_type,
            "curve_info": curve_info,
            "material_info": material_info,
            "data": data,
        })
    elif SnCurve.objects.filter(name=curve_name).exists():
        curve_info = SnCurve.objects.get(name=curve_name)
        data = Graph().sn_curve(curve_info)
        return render(response, "main/sn_curve.html", {
            "material_type": material_type,
            "curve_info": curve_info,
            "material_info": material_info,
            "data": data,
        })
    elif StaticCurve.objects.filter(name=curve_name).exists():
        curve_info = StaticCurve.objects.get(name=curve_name)
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
    context = {"material_type_id": material_type_id, "material_info": material_info}
    return render(response, "main/delete_form.html", context)


###   CREATE/ADD/EDIT HOSE   ###
def create_hose(response, material_type_id):
    form = HoseForm()
    form_s = HoseStaticForm()
    form_d = HoseDynamicForm()
    if response.method == "POST":
        form = HoseForm(response.POST)
        form_s = HoseStaticForm(response.POST)
        form_d = HoseDynamicForm(response.POST)
        if form.is_valid() and form_s.is_valid() and form_d.is_valid():
            # base #
            cleaned_data = form.cleaned_data
            cleaned_data["material_type_id"] = MaterialType.objects.get(pk=material_type_id)
            hose_model = Hose(**cleaned_data)
            hose_model.save()

            # static #
            cleaned_data_s = form_s.cleaned_data
            cleaned_data_s["Stat_hose_id"] = Hose.objects.get(pk=hose_model.id)
            hose_model_s = HoseStatic(**cleaned_data_s)
            hose_model_s.save()

            # dynamic #
            cleaned_data_d = form_d.cleaned_data
            cleaned_data_d["Dyn_hose_id"] = Hose.objects.get(pk=hose_model.id)
            hose_model_d = HoseDynamic(**cleaned_data_d)
            hose_model_d.save()

            return redirect('/material_type_list/%s' % material_type_id)
    context = {"form": form, "form_s": form_s, "form_d": form_d, "material_type_id": material_type_id}
    return render(response, "main/add_update_form.html", context)


def update_hose(response, material_type_id, hose_id):
    hose_info = Hose.objects.get(pk=hose_id)
    hose_info_s = HoseStatic.objects.get(Stat_hose_id=hose_id)
    hose_info_d = HoseDynamic.objects.get(Dyn_hose_id=hose_id)
    form = HoseForm(instance=hose_info)
    form_s = HoseStaticForm(instance=hose_info_s)
    form_d = HoseDynamicForm(instance=hose_info_d)
    if response.method == "POST":
        form = HoseForm(response.POST, instance=hose_info)
        form_s = HoseStaticForm(response.POST, instance=hose_info_s)
        form_d = HoseDynamicForm(response.POST, instance=hose_info_d)
        if form.is_valid() and form_s.is_valid() and form_d.is_valid():
            form.save()
            form_s.save()
            form_d.save()

            return redirect('/material_type_list/%s' % material_type_id)
    context = {"form": form, "form_s": form_s, "form_d": form_d, "material_type_id": material_type_id}
    return render(response, "main/add_update_form.html", context)


def delete_hose(response, material_type_id, hose_id):
    hose_info = Hose.objects.get(pk=hose_id)
    if response.method == "POST":
        hose_info.delete()
        return redirect('/material_type_list/%s' % material_type_id)
    context = {"material_type_id": material_type_id, "material_info": hose_info}
    return render(response, "main/delete_form.html", context)


###   CREATE/ADD/EDIT CURVE STATIC   ###
def create_static_curve(response, material_type_id, material_id):
    form = StaticCurveForm()
    if response.method == "POST":
        form = StaticCurveForm(response.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data["material_id"] = Material.objects.get(pk=material_id)
            static_model = StaticCurve(**cleaned_data)
            static_model.save()
            return redirect('material_info', material_type_id=material_type_id, material_id=material_id)
    context = {"form": form, "material_type_id": material_type_id, "material_id": material_id}
    return render(response, "main/add_update_form.html", context)


def create_cyclic_curve(response, material_type_id, material_id):
    form = CyclicCurveForm()
    if response.method == "POST":
        form = CyclicCurveForm(response.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data["material_id"] = Material.objects.get(pk=material_id)
            cyclic_model = CyclicCurve(**cleaned_data)
            cyclic_model.save()
            return redirect('material_info', material_type_id=material_type_id, material_id=material_id)
    context = {"form": form, "material_type_id": material_type_id, "material_id": material_id}
    return render(response, "main/add_update_form.html", context)


def create_en_curve(response, material_type_id, material_id):
    form = EnCurveForm()
    if response.method == "POST":
        form = EnCurveForm(response.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data["material_id"] = Material.objects.get(pk=material_id)
            en_model = EnCurve(**cleaned_data)
            en_model.save()
            return redirect('material_info', material_type_id=material_type_id, material_id=material_id)
    context = {"form": form, "material_type_id": material_type_id, "material_id": material_id}
    return render(response, "main/add_update_form.html", context)


def create_sn_curve(response, material_type_id, material_id):
    form = SnCurveForm()
    if response.method == "POST":
        form = SnCurveForm(response.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data["material_id"] = Material.objects.get(pk=material_id)
            sn_model = SnCurve(**cleaned_data)
            sn_model.save()
            return redirect('material_info', material_type_id=material_type_id, material_id=material_id)
    context = {"form": form, "material_type_id": material_type_id, "material_id": material_id}
    return render(response, "main/add_update_form.html", context)


def update_curve(response, material_type_id, material_id, curve_name):
    if StaticCurve.objects.filter(name=curve_name).exists():
        curve_info_s = StaticCurve.objects.get(name=curve_name)
        form = StaticCurveForm(instance=curve_info_s)
        if response.method == "POST":
            form = StaticCurveForm(response.POST, instance=curve_info_s)
            if form.is_valid():
                form.save()
                return redirect('material_info', material_type_id=material_type_id, material_id=material_id)
    elif CyclicCurve.objects.filter(name=curve_name).exists():
        curve_info_c = CyclicCurve.objects.get(name=curve_name)
        form = StaticCurveForm(instance=curve_info_c)
        if response.method == "POST":
            form = CyclicCurveForm(response.POST, instance=curve_info_c)
            if form.is_valid():
                form.save()
                return redirect('material_info', material_type_id=material_type_id, material_id=material_id)
    elif EnCurve.objects.filter(name=curve_name).exists():
        curve_info_e = EnCurve.objects.get(name=curve_name)
        form = EnCurveForm(instance=curve_info_e)
        if response.method == "POST":
            form = EnCurveForm(response.POST, instance=curve_info_e)
            if form.is_valid():
                form.save()
                return redirect('material_info', material_type_id=material_type_id, material_id=material_id)
    elif SnCurve.objects.filter(name=curve_name).exists():
        curve_info_s = SnCurve.objects.get(name=curve_name)
        form = SnCurveForm(instance=curve_info_s)
        if response.method == "POST":
            form = SnCurveForm(response.POST, instance=curve_info_s)
            if form.is_valid():
                form.save()
                return redirect('material_info', material_type_id=material_type_id, material_id=material_id)
    context = {"form": form, "material_type_id": material_type_id, "material_id": material_id}
    return render(response, "main/add_update_form.html", context)


def delete_curve(response, material_type_id, material_id, curve_name):
    material_info = {"name":curve_name}
    if StaticCurve.objects.filter(name=curve_name).exists():
        curve_info = StaticCurve.objects.get(name=curve_name)
        if response.method == "POST":
            curve_info.delete()
            return redirect('material_info', material_type_id=material_type_id, material_id=material_id)
    elif CyclicCurve.objects.filter(name=curve_name).exists():
        curve_info = CyclicCurve.objects.get(name=curve_name)
        if response.method == "POST":
            curve_info.delete()
            return redirect('material_info', material_type_id=material_type_id, material_id=material_id)
    elif EnCurve.objects.filter(name=curve_name).exists():
        curve_info = EnCurve.objects.get(name=curve_name)
        if response.method == "POST":
            curve_info.delete()
            return redirect('material_info', material_type_id=material_type_id, material_id=material_id)
    elif SnCurve.objects.filter(name=curve_name).exists():
        curve_info = SnCurve.objects.get(name=curve_name)
        if response.method == "POST":
            curve_info.delete()
            return redirect('material_info', material_type_id=material_type_id, material_id=material_id)
    context = {"material_type_id": material_type_id, "material_id": material_id, "material_info": material_info }
    return render(response, "main/delete_form.html", context)


def temperature_list(response, material_type_id, plastic_id, water_id):
    material_type = MaterialType.objects.get(pk=material_type_id)
    material_info = Plastic.objects.get(pk=plastic_id)
    water_info = WaterContent.objects.get(pk=water_id)
    temp_ls = Temperature.objects.filter(water_content_id=water_id)
    my_filter = TempFilter(response.GET, queryset=temp_ls)
    temp_ls = my_filter.qs
    return render(response, "main/temp_list.html", {
        "material_type": material_type,
        "material_info": material_info,
        "water_info": water_info,
        "water_ls": temp_ls,
        "my_filter": my_filter,
    })


def fibre_list(response, material_type_id, plastic_id, water_id, fibre_id):
    material_type = MaterialType.objects.get(pk=material_type_id)
    material_info = Plastic.objects.get(pk=plastic_id)
    water_info = WaterContent.objects.get(pk=water_id)
    temp_ls = Temperature.objects.filter(water_content_id=water_id)
    my_filter = TempFilter(response.GET, queryset=temp_ls)
    temp_ls = my_filter.qs
    return render(response, "main/temp_list.html", {
        "material_type": material_type,
        "material_info": material_info,
        "water_info": water_info,
        "water_ls": temp_ls,
        "my_filter": my_filter,
    })

