# helper/data_generator.py
import string
import random

def generate_unique_email(length=3):
    random_part = ''.join(random.choices(string.digits, k=length))
    return f"test1_{random_part}@yandex.ru"

def generate_name():
    names = ["Andrey"]
    return random.choice(names)

def generate_password():
    return "123456"

# словарь генератора
def prepare_user_credentials():
    
    return {
        "email": generate_unique_email(),
        "password": generate_password(),
        "name": generate_name(),
    }
