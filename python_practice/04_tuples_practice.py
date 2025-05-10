def solve_task_1():
    print("--- Задача 1 ---")
    countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
    last = countries[6]
    print(last)


def solve_task_2():
    print("--- Задача 2 ---")
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
    print(primes[:6])


def solve_task_3():
    print("--- Задача 3 ---")
    countries = (
        'Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
    print(countries[2:])


def solve_task_4():
    print("--- Задача 4 ---")
    countries = (
        'Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
    print(countries[:-3])


def solve_task_5():
    print("--- Задача 5 ---")
    city_name = input()
    city_year = int(input())
    city = (city_name, city_year)
    print(city)


def solve_task_6():
    print("--- Задача 6 ---")
    tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
    non_empty_tuples = [i for i in tuples if len(i) > 0]
    print(non_empty_tuples)


def solve_task_7():
    print("--- Задача 7 ---")
    # numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
    # averages = []
    #
    # for inner_tuple in numbers:
    #     current_sum = sum(inner_tuple)
    #     current_length = len(inner_tuple)
    #
    #     if current_length > 0:
    #         average = current_sum / current_length
    #     else:
    #         average = 0  #
    #
    #     averages.append(average)
    #
    # print(averages)

    numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

    averages = [sum(inner_tuple) / len(inner_tuple) if len(inner_tuple) > 0 else 0 for inner_tuple in numbers]

    print(averages)


if __name__ == "__main__":
    # solve_task_1()
    # solve_task_2()
    # solve_task_3()
    # solve_task_4()
    # solve_task_5()
    # solve_task_6()
    solve_task_7()
