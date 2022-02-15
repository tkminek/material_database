from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('material_type_list/', views.material_type_list, name="material_type_list"),
    path('material_type_list/<int:material_type_id>', views.material_list, name="material_list"),
]