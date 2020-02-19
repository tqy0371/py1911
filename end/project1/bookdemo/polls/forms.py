from django import forms
from .models import User

class LoginForm(forms.Form):
    """
    定义一个登录表单用于生成html登录表单
    """
    username = forms.CharField(max_length=150,min_length=6,label="输入用户名",
                               help_text="用户名最小6，最大150")
    password = forms.CharField(min_length=6,max_length=50,widget=forms.PasswordInput,
                               help_text="密码最小6，最大50",label="输入密码")


class RegistForm(forms.ModelForm):
    """
    定义一个注册表单用于生成html表单
    """
    password2 = forms.CharField(widget=forms.PasswordInput,label="重复密码")
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username':'输入用户名',
            'password':'输入密码',
        }
        help_texts = {
            'username':'长度为6-10位',
        }
        widgets = {
            'password':forms.PasswordInput,
        }