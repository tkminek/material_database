from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('material_type_list/', views.material_type_list, name="material_type_list"),
    path('material_type_list/steel_al/<int:material_type_id>/', views.material_list, name="material_list"),
    path('material_type_list/hose/<int:material_type_id>/', views.hose_list, name="hose_list"),
    path('material_type_list/plastic/<int:material_type_id>/', views.plastic_list, name="plastic_list"),
    path('material_type_list/rubber/<int:material_type_id>/', views.rubber_list, name="rubber_list"),
    path('material_type_list/steel_al/<int:material_type_id>/<int:material_id>', views.material_info, name="material_info"),
    path('material_type_list/hose/<int:material_type_id>/<int:hose_id>', views.hose_info, name="hose_info"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>', views.water_info, name="water_info"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>', views.rub_info, name="rub_info"),
    path('material_type_list/<int:material_type_id>/<int:material_id>/<str:curve_name>', views.curve_info, name="curve_info"),
    path('material_type_list/<int:material_type_id>/create_material/', views.create_material, name="create_material"),
    path('material_type_list/steel_al/<int:material_type_id>/<int:material_id>/update_material/', views.update_material, name="update_material"),
    path('material_type_list/steel_al/<int:material_type_id>/<int:material_id>/delete_material/', views.delete_material, name="delete_material"),
    path('material_type_list/hose/<int:material_type_id>/create_hose/', views.create_hose, name="create_hose"),
    path('material_type_list/hose/<int:material_type_id>/<int:hose_id>/update_hose/', views.update_hose, name="update_hose"),
    path('material_type_list/hose/<int:material_type_id>/<int:hose_id>/delete_hose/', views.delete_hose, name="delete_hose"),
    path('material_type_list/hose/<int:material_type_id>/<int:material_id>/create_static_curve/', views.create_static_curve, name="create_static_curve"),
    path('material_type_list/steel_al/<int:material_type_id>/<int:material_id>/create_cyclic_curve/', views.create_cyclic_curve, name="create_cyclic_curve"),
    path('material_type_list/steel_al/<int:material_type_id>/<int:material_id>/create_en_curve/', views.create_en_curve, name="create_en_curve"),
    path('material_type_list/steel_al/<int:material_type_id>/<int:material_id>/create_sn_curve/', views.create_sn_curve, name="create_sn_curve"),
    path('material_type_list/steel_al/<int:material_type_id>/<int:material_id>/<str:curve_name>/update_curve/', views.update_curve, name="update_curve"),
    path('material_type_list/steel_al/<int:material_type_id>/<int:material_id>/<str:curve_name>/delete_curve/', views.delete_curve, name="delete_curve"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/', views.temperature_list, name="temperature_list"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/<int:temp_id>/', views.fibre_list, name="fibre_list"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/<int:temp_id>/<int:fibre_id>/', views.fibre_info, name="fibre_info"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/<int:temp_id>/<int:fibre_id>/<str:curve_name>', views.fibre_curve_info, name="fibre_curve_info"),
    path('material_type_list/plastic/<int:material_type_id>/create_plastic/', views.create_plastic, name="create_plastic"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/update_plastic/', views.update_plastic, name="update_plastic"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/delete_plastic/', views.delete_plastic, name="delete_plastic"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/create_water/', views.create_water, name="create_water"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/update_water/', views.update_water, name="update_water"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/delete_water/', views.delete_water, name="delete_water"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/create_temp/', views.create_temp, name="create_temp"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/<int:temp_id>/update_temp/', views.update_temp, name="update_temp"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/<int:temp_id>/delete_temp/', views.delete_temp, name="delete_temp"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/<int:temp_id>/create_fibre/', views.create_fibre, name="create_fibre"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/<int:temp_id>/<int:fibre_id>/update_fibre/', views.update_fibre, name="update_fibre"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/<int:temp_id>/<int:fibre_id>/delete_fibre/', views.delete_fibre, name="delete_fibre"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/<int:temp_id>/<int:fibre_id>/create_static_curve_fibre/', views.create_static_curve_fibre, name="create_static_curve_fibre"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/<int:temp_id>/<int:fibre_id>/create_sn_curve_fibre/', views.create_sn_curve_fibre, name="create_sn_curve_fibre"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/<int:temp_id>/<int:fibre_id>/<str:curve_name>/update_curve_fibre/', views.update_curve_fibre, name="update_curve_fibre"),
    path('material_type_list/plastic/<int:material_type_id>/<int:plastic_id>/<int:water_id>/<int:temp_id>/<int:fibre_id>/<str:curve_name>/delete_curve_fibre/', views.delete_curve_fibre, name="delete_curve_fibre"),
    path('material_type_list/rubber/<int:material_type_id>/create_rubber/', views.create_rubber, name="create_rubber"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/update_rubber/', views.update_rubber, name="update_rubber"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/delete_rubber/', views.delete_rubber, name="delete_rubber"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/', views.rubber_temp_list, name="rubber_temp_list"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/create_rubber_temp/', views.create_rubber_temp, name="create_rubber_temp"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/<int:temp_id>/update_rubber_temp/', views.update_rubber_temp, name="update_rubber_temp"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/<int:temp_id>/delete_rubber_temp/', views.delete_rubber_temp, name="delete_rubber_temp"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/<int:temp_id>/', views.rubber_info, name="rubber_info"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/<int:temp_id>/create_arruda', views.create_arruda, name="create_arruda"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/<int:temp_id>/create_mooney', views.create_mooney, name="create_mooney"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/<int:temp_id>/create_polynomial', views.create_polynomial, name="create_polynomial"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/<int:temp_id>/create_yeoh', views.create_yeoh, name="create_yeoh"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/<int:temp_id>/create_ogden', views.create_ogden, name="create_ogden"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/<int:temp_id>/create_neo_hooke', views.create_neo_hooke, name="create_neo_hooke"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/<int:temp_id>/<str:model_name>/update_model', views.update_model, name="update_model"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/<int:temp_id>/<str:model_name>/delete_model', views.delete_model, name="delete_model"),
    path('material_type_list/rubber/<int:material_type_id>/<int:rubber_id>/<int:temp_id>/<str:model_name>/model_info', views.model_info, name="model_info"),
]