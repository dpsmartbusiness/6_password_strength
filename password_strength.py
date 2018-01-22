import sys
import re
import getpass


def load_blacklist_file(file_path):
    with open(file_path, 'r', encoding='UTF-8') as blacklist_file:
        return blacklist_file.read().splitlines()


def is_empty_password(password):
    return bool(re.search('r', password))


def check_password_length(password):
    min_password_length = 6
    return len(password) > min_password_length


def is_upper_case(password):
    return bool(re.search(r'[A-Z]', password))


def is_lower_case(password):
    return bool(re.search(r'[a-z]', password))


def is_numbers(password):
    return bool(re.search(r'\d', password))


def is_symbols(password):
    return bool(re.search(r'\W', password))


def is_not_phone_number(password):
    return not bool(re.search(r'[7-8]\d{10}', password))


def is_not_date(password):
    return not bool(re.search(r'\d{1,2}[-.]\d{1,2}[-.]\d{2,4}', password))


def get_password_strength(user_password, password_black_list):
    strength_points_score = 0
    if user_password in password_black_list:
        return '{}-password from blacklist'.format(strength_points_score)
    else:
        strength_password_criteria = [
            is_empty_password,
            check_password_length,
            is_upper_case,
            is_lower_case,
            is_numbers,
            is_symbols,
            is_not_phone_number,
            is_not_date
        ]
        for request in strength_password_criteria:
            if request(user_password):
                strength_points_score += 1
        return strength_points_score


if __name__ == '__main__':
    user_password = getpass.getpass('Type your password: ')
    password_black_list = load_blacklist_file(sys.argv[1])
    strength_points = get_password_strength(
        user_password,
        password_black_list
    )
    print ('User\'s password: {}'.format(user_password))
    print ('Password strength score: {}'.format(strength_points))