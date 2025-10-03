from django.shortcuts import render

def index(request):
    proveedores = [
        {'nombre': 'Proveedor A', 'producto': 'Componentes Electrónicos', 'contacto': 'proveedorA@example.com'},
        {'nombre': 'Proveedor B', 'producto': 'Material de Oficina', 'contacto': 'proveedorB@example.com'},
        {'nombre': 'Proveedor C', 'producto': 'Servicios de Limpieza', 'contacto': 'proveedorC@example.com'},
    ]
    contexto = {'proveedores': proveedores}
    return render(request, 'index.html', contexto)