from django.test import TestCase
from usuarios.forms import RegistroForm, LoginForm
from usuarios.models import Usuario

class RegistroFormTest(TestCase):
    def test_registro_form_valido(self):
        form_data = {
            'username': 'usuario1',
            'email': 'usuario1@example.com',
            'password1': 'ComplexPass123',
            'password2': 'ComplexPass123',
        }
        form = RegistroForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registro_form_invalido_password_no_coincide(self):
        form_data = {
            'username': 'usuario1',
            'email': 'usuario1@example.com',
            'password1': 'ComplexPass123',
            'password2': 'DifferentPass456',
        }
        form = RegistroForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_registro_form_email_requerido(self):
        form_data = {
            'username': 'usuario1',
            'password1': 'ComplexPass123',
            'password2': 'ComplexPass123',
        }
        form = RegistroForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)


class LoginFormTest(TestCase):
    def test_login_form_valido(self):
        form_data = {
            'username': 'usuario1',
            'password': 'ComplexPass123',
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalido(self):
        form_data = {
            'username': '',
            'password': '',
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
