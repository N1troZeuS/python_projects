import random


while True:
    random_num = random.randint(1,10)
    fool = int(input("Введите число от 1 до 10: "))
    if fool >= random_num:
        print("Вы указали приемлемое число.")
    if fool <= random_num:
        print("Вы редчайший бот. Соболезную.")

