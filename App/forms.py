from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Usuario'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña', 'id': 'password-field'}))
	remember_me = forms.BooleanField(required=False, initial=True)