def solve_task_1():
    print("--- Задача 1 ---")
    my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa',
               10.12: [1, 2, 3], 99.0: {9, 0, 1}}
    summary = max(my_dict) + min(my_dict)
    print(summary)


def solve_task_2():
    print("--- Задача 2 ---")
    result = {}
    for num in range(1, 16):
        result[num] = num ** 2
    print(result)


def solve_task3_v1():
    print("--- Задача 3 Версия 1 ---")
    text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
    result = {}
    for i in text:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1


def solve_task3_v2():
    print("--- Задача 3 Версия 2 ---")
    text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
    result = {}
    for i in text:
        result[i] = result.setdefault(i, 0) + 1
    print(result)


def solve_task_4():
    print("--- Задача 4 ---")
    users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
             {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
             {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
             {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
             {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
             {'name': 'John', 'phone': '233-421-32', 'email': ''},
             {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
             {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
             {'name': 'Robert', 'phone': '420-2011', 'email': ''},
             {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
             {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
             {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
             {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
             {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
             {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
             {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
    names_ending_with_8 = []

    for user_data in users:
        if user_data["phone"][-1] == "8":
            names_ending_with_8.append(user_data["name"])

    sorted_names = sorted(names_ending_with_8)
    print(*sorted_names)


def solve_task_5():
    print("--- Задача 5 ---")
    numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
    result = {i: numbers[i] ** 2 for i in range(len(numbers))}
    print(result)


def solve_task_6():
    print("--- Задача 6 ---")
    digit_map = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }

    number_string = input()

    word_list = []
    for digit_character in number_string:
        word_for_digit = digit_map[digit_character]
        word_list.append(word_for_digit)

    result_string = " ".join(word_list)
    print(result_string)


def solve_task_7():
    print("--- Задача 7 ---")
    n = input()
    courses = {'CS101': '3004, Хайнс, 8:00',
               'CS102': '4501, Альварадо, 9:00',
               'CS103': '6755, Рич, 10:00',
               'NT110': '1244, Берк, 11:00',
               'CM241': '1411, Ли, 13:00'}
    print(f'{n}: {courses[n]}')


if __name__ == "__main__":
    # solve_task_1()
    # solve_task_2()
    # solve_task3_v1()
    # solve_task3_v2()
    # solve_task_4()
    # solve_task_5()
    solve_task_6()
    # solve_task_7()
