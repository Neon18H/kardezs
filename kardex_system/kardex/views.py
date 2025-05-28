from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Compra
from .forms import CompraForm
from django.contrib import messages

@login_required
def kardex_view(request):
    compras = Compra.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'kardex/kardex.html', {
        'compras': compras,
        'saldo': request.user.saldo
    })

@login_required
def agregar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.usuario = request.user
            compra.save()
            messages.success(request, "Compra registrada exitosamente!")
            return redirect('kardex')
    else:
        form = CompraForm()
    return render(request, 'kardex/agregar_compra.html', {'form': form})

from django.contrib.auth.decorators import user_passes_test
from usuarios.models import Usuario

@user_passes_test(lambda u: u.is_superuser)
def admin_kardex_view(request):
    usuarios = Usuario.objects.all().order_by('-saldo')
    total_general = sum(usuario.saldo for usuario in usuarios)

    return render(request, 'kardex/admin_kardex.html', {
        'usuarios': usuarios,
        'total_general': total_general
    })

@login_required
def kardex_view(request):
    user_id = request.GET.get('user_id')
    if user_id and request.user.is_superuser:
        usuario = get_object_or_404(Usuario, pk=user_id)
    else:
        usuario = request.user

    compras = Compra.objects.filter(usuario=usuario).order_by('-fecha')

    return render(request, 'kardex/kardex.html', {
        'compras': compras,
        'saldo': usuario.saldo,
        'usuario_actual': usuario
    })
