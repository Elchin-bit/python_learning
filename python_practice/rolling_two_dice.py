import random

MIN_VAL = 1
MAX_VAL = 6

def roll_die():
    roll_result = random.randint(MIN_VAL, MAX_VAL)
    print(roll_result)
    return roll_result

def main():
    again = 'д'

    while again.lower() == 'д':
        print('Бросаем кубики...')
        print('Значение граней:')
        roll_die()
        roll_die()

        again = input('Бросить кубики ещё раз? (д = да): ')

if __name__ == '__main__':
    main()