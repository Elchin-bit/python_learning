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

if __name__ == "__main__":
    # solve_task_1()
    # solve_task_2()
    # solve_task3_v1()
     solve_task3_v2()
