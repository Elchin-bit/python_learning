def merge_lists(list1, list2):
    print("--- Задача: Отсортированный список")
    list1.extend(list2)
    print(sorted(list1))

def merge_lists2():
    print("--- Задача: Отсортированный список 2")
    all_lines_data = []
    n = int(input())
    for i in range(n):
        current_line_numbers = [int(c) for c in input().split()]
        all_lines_data.extend(current_line_numbers)
        all_lines_data.sort()
    print(all_lines_data)



if __name__ == "__main__":
    # merge_lists([int(c) for c in input().split()], [int(c) for c in input().split()])
    merge_lists2()


