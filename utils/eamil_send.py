from random import Random

from django.shortcuts import render
from django.core.mail import send_mail

from lambert.settings import EMAIL_FROM
from users.models import EmailVerifyRecord
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_email(email,send_type="register"):
    email_record = EmailVerifyRecord()
    active_code = random_str(20)
    email_record.code = active_code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_subject = "25years.xyz 注册激活链接"
        email_message = "请点击下面的链接激活你的账号：http://localhost:8000/active/%s/"%active_code

        send_status = send_mail(email_subject,email_message,EMAIL_FROM,[email])

        if send_status:
            pass
            print("发邮件成功")


