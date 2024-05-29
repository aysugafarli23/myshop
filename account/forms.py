from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, label = "İstifadəçi adı")
    password = forms.CharField(max_length=20, required = True, label = "Şifrə" , widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, required=True, label = "Şifrənin təkrarı", widget = forms.PasswordInput)
    
    def clean_field(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        
        data = {
            "username": username,
            "password": password
        } 
        
        return data


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50, label = "İstifadəçi adı")
    password = forms.CharField(max_length = 20, label = "Şifrə", widget=forms.PasswordInput)
    
