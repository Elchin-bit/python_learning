import math
import re
from itertools import count


def merge_lists(list1, list2):
    print("--- Задача: Отсортированный список ---")
    list1.extend(list2)
    print(sorted(list1))


def merge_lists2():
    print("--- Задача: Отсортированный список 2 ---")
    all_lines_data = []
    n = int(input())
    for i in range(n):
        current_line_numbers = [int(c) for c in input().split()]
        all_lines_data.extend(current_line_numbers)
    all_lines_data.sort()
    return all_lines_data


def is_valid_triangle(side1, side2, side3):
    print("--- Задача: Невырожденный треугольник ---")
    if (side1 + side2 > side3) and \
            (side1 + side3 > side2) and \
            (side2 + side3 > side1):
        return True
    else:
        return False


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_next_prime(num):
    next_num = num + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1


def is_password_good(password):
    has_upper = False
    has_lower = False
    has_digit = False

    if len(password) < 8:
        return False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit


def is_one_away(word1, word2):
    count = 0
    if word1 == word2 or len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            count += 1
    if len(word1) - count == 1:
        return True
    else:
        return False


def is_palindrome(text):
    text_lower = text.lower()
    cleaned_text = ""
    for char in text_lower:
        if char.isalpha():
            cleaned_text += char

    return cleaned_text == cleaned_text[::-1]


def is_valid_password(password):
    parts = password.split(':')

    if len(parts) != 3:
        return False

    a_str, b_str, c_str = parts[0], parts[1], parts[2]

    if not (a_str.isdigit() and b_str.isdigit() and c_str.isdigit()):
        return False

    a_num = int(a_str)
    b_num = int(b_str)
    c_num = int(c_str)

    if not (a_num > 0 and b_num > 0 and c_num > 0):
        return False

    condition_a = (a_str == a_str[::-1])

    condition_b = is_prime(b_num)

    condition_c = (c_num % 2 == 0)

    return condition_a and condition_b and condition_c


def is_correct_bracket(text):
    count = 0
    for char in text:
        if char == ')':
            count -= 1
            if count < 0:
                return False
        elif char == '(':
            count += 1

    return count == 0


def convert_to_python_case(text):
    if not text:
        return ""

    new_text = text[0].lower()

    for char in text[1:]:
        if char.isupper():
            new_text += "_" + char.lower()
        else:
            new_text += char

    return new_text


def get_middle_point(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y


def get_circle(radius):
    C = 2 * math.pi * radius
    S = math.pi * radius ** 2

    return C, S


def solve(a, b, c):
    d = pow(b, 2) - 4 * a * c
    if d < 0:
        return False
    elif d == 0:
        x = -(b / (2 * a))
        return x, x
    else:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        if x1 < x2:
            return x1, x2
        else:
            return x2, x1


if __name__ == "__main__":
    # merge_lists([int(c) for c in input().split()], [int(c) for c in input().split()])
    # print(merge_lists2())

    # --- Код для задачи с треугольником ---
    # a, b, c = int(input()), int(input()), int(input())
    # result = is_valid_triangle(a, b, c)
    # print(result)

    # --- Код для задачи с простым числом 1 ---
    # n = int(input())
    # print(is_prime(n))

    # --- Код для задачи с простым числом 2 ---
    # print("--- Задача: Найти простое число ---")
    # n = int(input())
    # print(get_next_prime(n)

    # --- Код для задачи: Хороший пароль ---
    # txt = input()
    # print(is_password_good(txt))

    # --- Код для задачи: Ровно в одном ---
    # txt1 = input()
    # txt2 = input()
    # print(is_one_away(txt1, txt2))

    # --- Код для задачи: Палиндром ---
    # txt = input()
    # print(is_palindrome(txt))

    # --- Код для задачи: Проверка пароля ---
    # psw = input()
    # print(is_valid_password(psw))

    # --- Код для задачи: Правильная скобочная последовательность ---
    # txt = input()
    # print(is_correct_bracket(txt))

    # --- Код для задачи: Змеиный регистр ---
    # txt = input()
    # print(convert_to_python_case(txt))

    # --- Код для задачи: Середина отрезка ---
    # x_1, y_1 = int(input()), int(input())
    # x_2, y_2 = int(input()), int(input())
    # x, y = get_middle_point(x_1, y_1, x_2, y_2)
    # print(x, y)

    # --- Код для задачи: Площадь и длина ---
    # r = float(input())
    # length, square = get_circle(r)
    # print(length, square)

    # --- Код для задачи: Корни управления ---
    a, b, c = int(input()), int(input()), int(input())
    x1, x2 = solve(a, b, c)
    print(x1, x2)
