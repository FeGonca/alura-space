from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        max_length=100, 
        label='Nome de Login', 
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ex.: João Silva'}))
    
    senha = forms.CharField(
        max_length=70, 
        label='Senha', 
        required=True, 
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Digite sua senha'}))
    
class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        max_length=100, 
        label='Nome de Cadastro', 
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ex.: João Silva'}))
    
    email = forms.EmailField(
        max_length=100, 
        label='E-mail', 
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ex.: joaosilva@gmail.com'}))
    
    senha_1 = forms.CharField(
        max_length=70, 
        label='Senha', 
        required=True, 
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Digite sua senha'}))
    
    senha_2 = forms.CharField(
        max_length=70, 
        label='Confirme sua senha', 
        required=True, 
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Digite sua senha novamente'}))