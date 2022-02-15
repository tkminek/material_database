from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import MaterialType,Material,SnCurve,EnCurve,CyclicCurve


def home(response):
    return HttpResponse("Home page")


def material_list(response):
    return HttpResponse("material_list")


def material_info(response,id):
    return HttpResponse(f"{id}")