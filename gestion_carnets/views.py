from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Beneficiario
from .forms import BeneficiarioForm 

@login_required
def inicio(request):
    # Traemos la lista ordenada para que los nuevos aparezcan arriba
    lista = Beneficiario.objects.all().order_by('-id')
    
    if request.method == 'POST':
        form = BeneficiarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = BeneficiarioForm()

    # Lógica para permisos (Basado en tus grupos de Django)
    puede_registrar = request.user.groups.filter(name='Recepcion').exists() or request.user.is_superuser
    
    context = {
        'lista': lista,
        'form': form,
        'puede_registrar': puede_registrar,
    }
    return render(request, 'lista.html', context)

@login_required
def editar_beneficiario(request, beneficiario_id):
    beneficiario = get_object_or_404(Beneficiario, id=beneficiario_id)
    if request.method == 'POST':
        # Al pasar instance=beneficiario, Django sabe que debe actualizar y no crear uno nuevo
        form = BeneficiarioForm(request.POST, instance=beneficiario)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = BeneficiarioForm(instance=beneficiario)
    
    return render(request, 'editar.html', {'form': form, 'beneficiario': beneficiario})

@login_required
def eliminar_beneficiario(request, beneficiario_id):
    beneficiario = get_object_or_404(Beneficiario, id=beneficiario_id)
    beneficiario.delete()
    return redirect('inicio')

@login_required
def cargar_examen(request, beneficiario_id):
    beneficiario = get_object_or_404(Beneficiario, id=beneficiario_id)
    return render(request, 'cargar_examen.html', {'b': beneficiario})

@login_required
def revision_medica(request, beneficiario_id):
    beneficiario = get_object_or_404(Beneficiario, id=beneficiario_id)
    return render(request, 'revision_medica.html', {'b': beneficiario})

@login_required
def generar_pdf_carnet(request, beneficiario_id):
    # Esta ruta ya está lista para recibir tu lógica de ReportLab o WeasyPrint
    return redirect('inicio')

def salir(request):
    logout(request)
    return redirect('login')