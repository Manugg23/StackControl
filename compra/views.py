from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .forms import AgregarProductoForm, AgregarProveedorForm
from .models import Producto, Proveedor
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required




def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    usuario = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                    usuario.save()
                    login(request, usuario)
                    return redirect('home')
                except:
                    return render(request, 'signup.html', {'form': UserCreationForm, 'error':'ERROR: El usuario ya existe'})
            return render(request, 'signup.html', {'form': UserCreationForm, 'error':'ERROR: Las contraseñas no coinciden'})

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm})
    else:
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'login.html', {'form': AuthenticationForm, 'error':'Error: El usuario o contraseña es incorrecto'})
        else:
            login(request, usuario)
            return redirect('home')
    
    return render(request, 'login.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('login')



def Home(request):
    return render(request, 'home.html')





@login_required
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'mostrar_proveedores.html', {'proveedores' : proveedores})

@login_required
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'mostrar_productos.html', {'productos': productos})

@login_required
def listar_todos(request):
    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()
    return render(request, 'mostrar_todo.html', {'proveedores' :proveedores, 'productos':productos})




@login_required
def detalle_proveedor(request, proveedor_id):
    if request.method == 'GET':
        proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
        form = AgregarProveedorForm(instance=proveedor)
        return render(request, 'detalle_proveedor.html', {'proveedor': proveedor, 'form': form})
    else:
        try:
            proveedor = get_object_or_404(Proveedor, pk = proveedor_id)
            formulario = AgregarProveedorForm(request.POST, instance=proveedor)
            formulario.save()
            return redirect('listar_proveedores')
        except ValueError:
            return render(request, 'detalle_proveedor.html', {'proveedor': proveedor , 'form': form, 'error': 'Error en los datos para actualizar.'})

@login_required
def detalle_producto(request, producto_id):
    if request.method == 'GET':
        proveedores = Proveedor.objects.all()
        producto = get_object_or_404(Producto, pk=producto_id)
        form = AgregarProductoForm(instance=producto)
        return render(request, 'detalle_producto.html', {'producto': producto, 'form': form, 'proveedores': proveedores })
    else:
        try:
            producto = get_object_or_404(Producto, pk = producto_id)
            formulario = AgregarProductoForm(request.POST, instance=producto)
            formulario.save()
            return redirect('listar_productos')
        except ValueError:
            return render(request, 'detalle_producto.html', {'producto': producto , 'form': form, 'error': 'Error en los datos para actualizar.'})



@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    producto.delete()
    return redirect('listar_productos')


@login_required
def eliminar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    proveedor.delete()
    return redirect('listar_proveedores')




@login_required
def agregar_producto(request):
    
    if request.method == 'GET':
        proveedores = Proveedor.objects.all()
        return render(request, 'agregar_producto.html', {'form': AgregarProductoForm, 'proveedores': proveedores})
    else:
        try:
            form = AgregarProductoForm(request.POST)
            nuevo_producto = form.save(commit=False)
            nuevo_producto.save()
            return redirect('listar_productos')
        except ValueError:
            return render(request, 'agregar_producto.html', {
                'form': AgregarProductoForm,
                'error': 'Por favor, ingrese datos válidos'
                })


@login_required
def agregar_proveedor(request):
    
    if request.method == 'GET':
        return render(request, 'agregar_proveedor.html', {'form': AgregarProveedorForm})
    else:
        try:
            form = AgregarProveedorForm(request.POST)
            nuevo_proveedor = form.save(commit=False)
            nuevo_proveedor.save()
            return redirect('listar_proveedores')
        except ValueError:
            return render(request, 'agregar_proveedor.html', {
                'form': AgregarProductoForm,
                'error': 'Por favor, ingrese datos válidos'
                })

