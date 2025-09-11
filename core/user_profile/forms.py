from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User=get_user_model()

class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'رمز عبور',
            'required': 'required',
            'class': 'form-control'
        })
    )
    password2 = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'تکرار رمز عبور',
            'required': 'required',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ["user_name", "email", "password1", "password2"]
        widgets = {
            'user_name': forms.TextInput(attrs={
                'placeholder': 'نام کاربری',
                'required': 'required',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'ایمیل خود را وارد کنید',
                'required': 'required',
                'class': 'form-control',
            })
        }
        labels = {
            'user_name': 'نام کاربری',
            'email': 'ایمیل'
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("این ایمیل قبلاً ثبت شده است.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("رمز عبور و تکرار آن یکی نیستند!")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False  
        if commit:
            user.save()
        return user
    

class LoginForm(forms.Form):
    user_name = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'})
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'})
    )

    def clean(self):
        cleaned_data = super().clean()
        user_name = cleaned_data.get('user_name')
        password = cleaned_data.get('password')

        if user_name and password:
            user = authenticate(username=user_name, password=password)
            if user is None:
                raise forms.ValidationError("نام کاربری یا رمز عبور اشتباه است.")
            if not user.is_active:
                raise forms.ValidationError("حساب کاربری شما فعال نیست.")
            cleaned_data['user'] = user
        return cleaned_data