from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('material_type_list/', views.material_type_list, name="material_type_list"),
    path('material_type_list/<int:material_type_id>', views.material_list, name= "material_list"),
    path('material_type_list/<int:material_type_id>/<int:material_id>', views.material_info, name="material_info"),
    path('material_type_list/<int:material_type_id>/<int:material_id>/<str:curve_name>', views.curve_info, name="curve_info"),
    path('material_type_list/<int:material_type_id>/create_material/', views.create_material, name="create_material"),
    path('material_type_list/<int:material_type_id>/<int:material_id>/update_material/', views.update_material, name="update_material"),
    path('material_type_list/<int:material_type_id>/<int:material_id>/delete_material/', views.delete_material, name="delete_material"),
]