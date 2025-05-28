import math


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
    print("--- Задача: Найти простое число ---")
    n = int(input())
    print(get_next_prime(n))
