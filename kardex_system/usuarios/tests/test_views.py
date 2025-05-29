from django.test import TestCase, Client
from django.urls import reverse
from usuarios.models import Usuario

class UsuariosViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Usuario.objects.create_user(username='usuario1', password='pass')

    def test_registro_view_get(self):
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/registro.html')

    def test_registro_view_post_valido(self):
        response = self.client.post(reverse('registro'), {
            'username': 'nuevo_usuario',
            'email': 'nuevo@example.com',
            'password1': 'ComplexPass123',
            'password2': 'ComplexPass123',
        })
        self.assertRedirects(response, reverse('kardex'))
        self.assertTrue(Usuario.objects.filter(username='nuevo_usuario').exists())

    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/login.html')

    def test_login_view_post_valido(self):
        response = self.client.post(reverse('login'), {
            'username': 'usuario1',
            'password': 'pass',
        })
        self.assertRedirects(response, reverse('kardex'))

    def test_login_view_post_invalido(self):
        response = self.client.post(reverse('login'), {
            'username': 'usuario1',
            'password': 'wrongpass',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Usuario o contraseña incorrectos")

    def test_logout_view(self):
        self.client.login(username='usuario1', password='pass')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
