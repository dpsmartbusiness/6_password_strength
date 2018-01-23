import sys
import re
import getpass


def load_blacklist_file(file_path):
    with open(file_path, 'r', encoding='UTF-8') as blacklist_file:
        return blacklist_file.read().splitlines()


def is_not_empty_password(password):
    return bool(password)


def check_password_length(password):
    min_password_length = 6
    return len(password) > min_password_length


def has_upper_case(password):
    return bool(re.search(r'[A-Z]', password))


def has_lower_case(password):
    return bool(re.search(r'[a-z]', password))


def has_numbers(password):
    return bool(re.search(r'\d', password))


def has_symbols(password):
    return bool(re.search(r'\W', password))


def is_not_phone_number(password):
    return not bool(re.search(r'[7-8]\d{10}', password))


def is_not_date(password):
    return not bool(re.search(r'\d{1,2}[-.]\d{1,2}[-.]\d{2,4}', password))


def is_not_mail(password):
    return not bool(re.search(r'\w{1,30}[@]\w{1,10}[a-z][.][ru|com]', password))


def is_not_in_blacklist(password, black_list):
    return password not in black_list


def get_password_strength(user_password, password_black_list):
    strength_points_score = 0
    if not is_not_in_blacklist(user_password, password_black_list):
        return '{}-password from blacklist'.format(strength_points_score)
    elif not is_not_empty_password(user_password):
        return 'You forgot to type a password. Try again.'
    else:
        strength_points_score += 1
        strength_password_criteria = [
            is_not_empty_password,
            check_password_length,
            has_upper_case,
            has_lower_case,
            has_numbers,
            has_symbols,
            is_not_phone_number,
            is_not_date,
            is_not_mail
        ]
        for strength_criteria in strength_password_criteria:
            if strength_criteria(user_password):
                strength_points_score += 1
        return strength_points_score


if __name__ == '__main__':
    try:
        password_black_list = load_blacklist_file(sys.argv[1])
        user_password = getpass.getpass('Type your password: ')
        strength_points = get_password_strength(
            user_password,
            password_black_list
        )
        print ('Password strength score: {}'.format(strength_points))
    except FileNotFoundError:
        print('Incorrect path to blacklist. Try again.')
    except IndexError:
        print ('Specify a path to blacklist. Try again.')