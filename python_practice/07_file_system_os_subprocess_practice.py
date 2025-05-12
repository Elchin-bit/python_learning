import os


def manage_test_folder(folder_name="my_os_test_folder"):
    print("--- Демонстрация работы с модулем os ---")

    print("\nСодержимое текущей директории")
    current_directory_content = os.listdir('.')
    if not current_directory_content:
        print("(пусто)")
    else:
        for item in current_directory_content:
            print(item)

    print(f"\nСоздаем папку: {folder_name}")
    if not os.path_exists(folder_name):
        os.mkdir(folder_name)
        print(f"Папка '{folder_name}' успешно создана")
    else:
        print(f"Папка '{folder_name}' уже существует")

    print(f"\nПроверяю наличие папки: {folder_name}")
    if os.path.exists(folder_name) and os.path.isdir(folder_name):
        print(f"Папка '{folder_name}' существует и является директорией")
    else:
        print(f"Что-то пошло не так: Папка '{folder_name}' Не найдена или это не та папка")

    print("-" * 30)




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


def input_line():
    print("--- Задача: Входная строка ---")
    text = input()
    with open('output.txt', 'w', encoding='UTF-8') as file:
        content = file.write(text)
    print(content)


def total_cost():
    print("--- Задача: Общая стоимость ---")
    total = 0
    with open('prices.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            cleaned_line = line.strip()

            parts = cleaned_line.split('\t')

            quantity_str = parts[1]
            price_str = parts[2]

            quantity = int(quantity_str)
            price_per_item = int(price_str)

            current_item_cost = quantity * price_per_item

            total += current_item_cost

    print(total)


def sum_of_the_numbers_in_the_rows():
    print("--- Задача: Сумма чисел в строках ---")
    with open('numbers.txt', 'r', encoding='UTF-8') as file:
        content = file.readlines()
        for line in content:
            parts = line.split()
            sum_for_this_line = sum(map(int, parts))
            print(sum_for_this_line)


def line_numbering():
    print("--- Задача: Нумерация строк ---")
    with open("input.txt", 'r', encoding='UTF-8') as input_file, open('output.txt', 'w',
                                                                      encoding='UTF-8') as output_file:
        content = input_file.readlines()
        for index, text in enumerate(content, start=1):
            cleaned_text_line = text.rstrip('\n')
            line_to_write = f'{index}) {cleaned_text_line}\n'
            output_file.write(line_to_write)


if __name__ == "__main__":
    # file_contents()
    # the_second_to_last_line()
    # the_sum_of_two_numbers()
    # input_line()
    # total_cost()
    # sum_of_the_numbers_in_the_rows()
    # line_numbering()
    manage_test_folder()
