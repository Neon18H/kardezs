from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def actualizar_saldo(self):
        from kardex.models import Compra  # Importación local para evitar circularidad
        total = Compra.objects.filter(usuario=self).aggregate(models.Sum('monto'))['monto__sum'] or 0
        self.saldo = total
        self.save()