from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.forms import EmailField, EmailInput
from django.forms import RegexField, TextInput, CharField, PasswordInput
from django.forms import ValidationError

class RegisterForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "비밀번호가 맞지 않습니다.",
    }

    email = EmailField(
        label='이메일',
        required=True,
        widget=EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required': 'True',
            }
        )
    )

    username = RegexField(
        label='아이디',
        max_length=30,
        regex='^[\w.@+-]+$',
        error_messages={
            'invalid': "숫자와 문자만 포함하세요"
        },
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'required': 'True',
            }
        ),
    )

    password1 = CharField(
        label='비밀번호',
        widget=PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        ),
    )

    password2 = CharField(
        label='비밀번호(확인)',
        widget=PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation',
                'required': 'True',
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)