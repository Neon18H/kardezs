from django import forms
from .models import Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['tipo_movimiento', 'descripcion', 'tienda', 'monto']
        widgets = {
            'descripcion': forms.TextInput(attrs={
                'placeholder': 'Ej. Zapatos deportivos',
                'class': 'form-control'
            }),
            'tienda': forms.TextInput(attrs={
                'placeholder': 'Ej. Tienda XYZ',
                'class': 'form-control'
            }),
            'monto': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
        }

    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        self.fields['tipo_movimiento'].widget.attrs.update({'class': 'form-select'})
