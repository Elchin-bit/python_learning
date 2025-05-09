def solve_task_1():
    print("--- Задача 1 ---")
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    list1[2][2].append(7000)
    print(list1)


def solve_task_2():
    print("--- Задача 2 ---")
    list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
    sub_list = ['h', 'i', 'j']
    list1[2][1][2].extend(sub_list)
    print(list1)


def solve_task_3():
    print("--- Задача 3 ---")
    list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
    maximum = []
    for i in list1:
        maximum.append(max(i))
    print(max(maximum))


def solve_task_4():
    print("--- Задача 4 ---")
    list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
    total = 0
    counter = 0
    for i in list1:
        total += sum(i)
        counter += len(i)
    print(total / counter)


def solve_task_5():
    print("--- Задача 5 ---")
    # numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
    # averages = []
    #
    # for inner_tuple in numbers:
    #
    #     current_sum = sum(inner_tuple)
    #
    #     current_length = len(inner_tuple)
    #
    #     if current_length > 0:
    #         average = current_sum / current_length
    #     else:
    #         average = 0
    #
    #     averages.append(average)
    #
    # print(averages)

    numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

    averages = [sum(inner_tuple) / len(inner_tuple) if len(inner_tuple) > 0 else 0 for inner_tuple in numbers]

    print(averages)


# --- Блок для вызова нужных функций ---
if __name__ == "__main__":
    # solve_task_1()
    # solve_task_2()
    # solve_task_3()
    # solve_task_4()
    solve_task_5()
