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
    path('material_type_list/<int:material_type_id>/create_hose/', views.create_hose, name="create_hose"),
    path('material_type_list/<int:material_type_id>/<int:hose_id>/update_hose/', views.update_hose, name="update_hose"),
    path('material_type_list/<int:material_type_id>/<int:hose_id>/delete_hose/', views.delete_hose, name="delete_hose"),
    path('material_type_list/<int:material_type_id>/<int:material_id>/create_static_curve/', views.create_static_curve, name="create_static_curve"),
    path('material_type_list/<int:material_type_id>/<int:material_id>/create_cyclic_curve/', views.create_cyclic_curve, name="create_cyclic_curve"),
    path('material_type_list/<int:material_type_id>/<int:material_id>/create_en_curve/', views.create_en_curve, name="create_en_curve"),
    path('material_type_list/<int:material_type_id>/<int:material_id>/create_sn_curve/', views.create_sn_curve, name="create_sn_curve"),
    path('material_type_list/<int:material_type_id>/<int:material_id>/<str:curve_name>/update_curve/', views.update_curve, name="update_curve"),
    path('material_type_list/<int:material_type_id>/<int:material_id>/<str:curve_name>/delete_curve/', views.delete_curve, name="delete_curve"),
]