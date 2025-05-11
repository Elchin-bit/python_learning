def file_contents():
    print("--- Задача: Содержимое файла ---")
    filename = input()
    with open(filename, 'r', encoding='UTF-8') as file_object:
        content = file_object.read()
        print(content)


def the_second_to_last_line():
    print("--- Задача: Предпоследняя строка ---")
    filename = input()
    with open(filename, 'r', encoding='UTF-8') as f:
        content = f.readlines()
        print(content[-2])


def the_sum_of_two_numbers():
    print("--- Задача: Сумма двух ---")
    with open('numbers.txt', 'r', encoding='UTF-8') as f:
        content = [int(i.rstrip()) for i in f.readlines()]
    print(sum(content))



if __name__ == "__main__":
    # file_contents()
    # the_second_to_last_line()
    the_sum_of_two_numbers()
