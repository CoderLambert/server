from django import forms
from  captcha.fields import CaptchaField
class LoginForm(forms.Form):
    """注意这里面定义的字段名要与form表单里面的name一样，否则无法识别取值"""
    user_name = forms.CharField(required=True)  #如果字段为空将会报错
    user_password = forms.CharField(required=True,min_length=5)

class RegisterForm(forms.Form):
    """注意这里面定义的字段名要与form表单里面的name一样，否则无法识别取值"""
    email = forms.EmailField(required=True)  #如果字段为空将会报错
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})#error_messages 要与captcha报的异常名一致
