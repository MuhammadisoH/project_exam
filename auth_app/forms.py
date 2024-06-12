from django import forms
from .models import Kirim

class KirimForm(forms.ModelForm):
    class Meta:
        model = Kirim
        fields = ['summa', 'sana', 'hisoblar', 'chiqim_turi']
