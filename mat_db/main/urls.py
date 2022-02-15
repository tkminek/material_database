from django.urls import path
from . import views



urlpatterns = [
    path('', views.home,name="home"),
    path('material_list/',views.material_list,name="material_list"),
    path('<int:id>', views.material_info,name="material_info"),
]