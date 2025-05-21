import random

HEADS = 1  # Орел
TAILS = 2  # Решка
TOSSES = 10  # Количество бросков


def main():
    for toss in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print('Орел')
        else:
            print('Решка')


if __name__ == '__main__':
    main()
