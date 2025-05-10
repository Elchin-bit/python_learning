def solve_task_1():
    print("--- Задача 1 ---")
    text = input()
    text_set = set(text)
    counter_unique = len(text_set)
    print(counter_unique)


def solve_task_2():
    print("--- Задача 2 ---")
    text1, text2 = input(), input()
    if set(text1) == set(text2):
        print("YES")
    else:
        print("NO")


def solve_task_3():
    print("--- Задача 3 ---")
    set1 = set(input().split())
    set2 = set(input().split())
    set1.intersection_update(set2)
    print(len(set1))


def solve_task_4():
    print("--- Задача 4 ---")
    set1 = set(map(int, input().split()))
    set2 = set(map(int, input().split()))
    set1.difference_update(set2)
    print(*sorted(set1))

def solve_task_5():
    print("--- Задача 5 ---")




if __name__ == "__main__":
    # solve_task_1()
    # solve_task_2()
    # solve_task_3()
    solve_task_4()
