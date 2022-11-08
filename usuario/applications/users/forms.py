from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegister."""
    
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' :'Contraseña'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' :'Repetir Contraseña'
            }
        )
    )

    class Meta:
        """Meta definition for UserRegisterform."""

        model = User
        fields = ('username',
                  'email',
                  'nombres',
                  'apellidos',
                  'genero',
            )


    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Ingrese contraseñas iguales')
        return super().clean()
    
    
class LoginForm(forms.Form):
      username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder' :'Nombre de usuario',
                'style': '{margin:10px)',
            }
        )
    )
      
      password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' :'Contraseña'
            }
        )
    )