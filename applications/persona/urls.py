
from django.contrib import admin
from django.urls import path
from . import views 

app_name='persona_app'

urlpatterns = [
    path('listar-todo-empleado/', views.ListAllEmpleados.as_view(),name='empleados_all'),
    path('listar-by-area/<shor_name>/', views.ListbyArea.as_view(),name='empleados_area'),
    path('listar-empleados-admin/', views.ListaEmpleadosAdmin.as_view(),name='empleados_admin'),
    path('buscar-empleado/', views.listEmpleadoByKword.as_view()),
    path('listar-habilidades-empleado/', views.HabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view(),name='empleado_detail'),
    path('add-empleado/', views.EmpleadoCreateView.as_view(),name='empleado_add'),
    path('success/', views.SuccessView.as_view(),name='correcto'),
    path('update-empleado/<pk>', views.EmpleadoUpdateView.as_view(),name='modificar_empleado'),
    path('delete-empleado/<pk>', views.EmpleadoDeleteView.as_view(),name='eliminar_empleado'),
    path('', views.InicioView.as_view(),name='inicio'),
    

    
]