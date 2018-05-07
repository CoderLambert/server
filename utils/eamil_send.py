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
    """发送邮件函数，以后还要考虑下安全性  邮件内容发送时加密 TTL """
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
        email_message = """尊敬的{active_email_name},您好！
请点击下面的链接激活您的账号,
http://www.25years.xyz/active/{email_actiive_code}/
                        
为保障您的帐号安全，请在24小时内点击该链接，您也可以将链接复制到浏览器地址访问。如果您并未尝试激活此帐号，请忽略本邮件，由此给您带来的不便请谅解。
                        
本邮件由系统自动发出，请勿直接回复！
""".format(active_email_name = email,email_actiive_code = active_code)
        print (email_message)

        send_status = send_mail(email_subject,email_message,EMAIL_FROM,[email])
        return send_status
        # #1：成功  0：错误
        # if send_status:
        #     #print("发邮件成功")
        #     return send_status
        # else:
        #     #print("发邮件失败")
        #     return send_status


