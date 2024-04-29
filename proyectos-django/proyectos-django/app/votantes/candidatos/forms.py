
from django import forms
from .models import Partido, Candidato
class FormCandidato(forms.ModelForm):
    
    class Meta:
        model = Candidato
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
            'apeido_Paterno': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido Paterno'
                }
            ),
            'apeido_Materno': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido Materno'
                }
            ),
            'partidos': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'imagen': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control-file',
                }
            ),
        }



class FormPartido(forms.ModelForm):
    
    class Meta:
        model = Partido
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
            'logo': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control-file',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción',
                    'rows': 3
                }
            ),
        }
class FormFiltrosCandidato(forms.Form):
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}))
    ap = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Apellido Paterno', 'class': 'form-control'}))
    am = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Apellido Materno', 'class': 'form-control'}))
    partidos = forms.ModelChoiceField(
        queryset=Candidato.objects.values_list('partidos', flat=True).distinct(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}))
class FormCandidatoEditar(FormPartido):
    class Meta:
        exclude = []
        model = Candidato
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
            'apeido_Paterno': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido Paterno'
                }
            ),
            'apeido_Materno': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido Materno'
                }
            ),
            'partidos': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'imagen': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control-file',
                }
            ),
        }
class FormEditarPartido(forms.ModelForm):
    
    class Meta:
        model = Partido
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
            'logo': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control-file',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción',
                    'rows': 3
                }
            ),
        }