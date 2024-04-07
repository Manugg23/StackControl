"""
URL configuration for StockControl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from compra import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.iniciar_sesion, name='login'),    
    path('logout/', views.cerrar_sesion, name='logout'),    
    path('', views.Home , name='home'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('todos/', views.listar_todos, name='listar_todos'),
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('proveedor/<int:proveedor_id>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('productos/<int:producto_id>/eliminar', views.eliminar_producto, name='eliminar_producto'),
    path('proveedor/<int:proveedor_id>/eliminar', views.eliminar_proveedor, name='eliminar_proveedor'),
]
