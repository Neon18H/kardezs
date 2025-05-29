from django.test import TestCase
from usuarios.models import Usuario
from kardex.models import Compra  
from django.db.models import Sum

class UsuarioModelTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_user(username='usuario1', password='pass')

    def test_actualizar_saldo_sin_compras(self):
        self.usuario.actualizar_saldo()
        self.assertEqual(self.usuario.saldo, 0)

    def test_actualizar_saldo_con_compras(self):
        # Crear compras asociadas al usuario
        Compra.objects.create(usuario=self.usuario, monto=100)
        Compra.objects.create(usuario=self.usuario, monto=50)
        self.usuario.actualizar_saldo()
        self.assertEqual(self.usuario.saldo, 150)
