'''Вспомогательные иснтрументы для API-тестов web-сервиса «Stellar Burgers».'''
import random
import string


def generate_username():
    '''Генерация имени пользователя.'''
    length = random.randint(6, 10)
    characters = string.ascii_lowercase
    return ''.join(random.choices(characters, k=length)).capitalize()


def generate_password():
    '''Генерация пароля.'''
    length = random.randint(8, 12)
    characters = string.digits + string.ascii_letters
    return ''.join(random.choices(characters, k=length))


def generate_email():
    '''Генерация email.'''
    prefix = {
        'chars': string.digits + string.ascii_lowercase,
        'min_max_len': (3, 10),
        'sep': '@'
    }
    domain = {
        'chars': string.ascii_lowercase,
        'min_max_len': (2, 7),
        'sep': '.'
    }
    zone = {
        'chars': string.ascii_lowercase,
        'min_max_len': (2, 3),
        'sep': ''
    }
    login = ''
    for segment in prefix, domain, zone:
        chars = segment['chars']
        length = random.randint(*segment['min_max_len'])
        login += ''.join(random.choices(chars, k=length)) + segment['sep']
    return login


def get_user_data():
    '''Получение данных для регистрации нового пользователя.'''
    return {
        'email': generate_email(),
        'password': generate_password(),
        'name': generate_username()
    }


if __name__ == '__main__':
    print(get_user_data())
