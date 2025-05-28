from django.db import models
from django.conf import settings  # Importamos desde settings en lugar de directamente

class Compra(models.Model):
    TIPO_MOVIMIENTO_CHOICES = [
        ('C', 'Compra'),
        ('D', 'Devolución'),
        ('A', 'Ajuste'),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='compras')
    fecha = models.DateTimeField(auto_now_add=True)
    tipo_movimiento = models.CharField(max_length=1, choices=TIPO_MOVIMIENTO_CHOICES, default='C')
    descripcion = models.CharField(max_length=100)
    tienda = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-fecha']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.usuario.actualizar_saldo()
