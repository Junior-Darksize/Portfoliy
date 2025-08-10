from django.core.mail import send_mail
from django.conf import settings



def send_email(receiver,code):

    res = send_mail("Tasdiqlash kodi",f"Poortfoliy saytidan emailingizni tasdiqlash uchun kod {code}",settings.DEFAULT_FROM_EMAIL,[receiver],fail_silently=False)
    print(res)