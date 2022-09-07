import random,requests
from django.conf import settings


def send_otp_to_phone(mobile):
    try:
        otp = random.randint(100000,999999)
        url = f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/{mobile}/{otp}'
        response = requests.get(url)
        print(response,"<---13---Response")
        return otp
    except Exception as e:
        return None
       