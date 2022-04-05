""""Вариант 1.
Написать программу, которая читая последовательность цифр из файла, вводит на экран четные цифры, стоящие на нечетных местах,
 повторяя каждую цифру так, чтобы число повторов равнялось номеру позиции цифры.
"""

import time

start = time.time()                                                 # запуск таймера

buffer_len = 1                                                      # размер буфера чтения
position = 0                                                        # номер позиции цифры

try:
    with open("prikol.txt", "r") as file:                           # открываем файл
        buffer = file.read(buffer_len)

        while buffer:                                               # пока в файле что-то есть
            while (buffer < '0' or buffer > '9') and buffer:        # поиск чисел
                buffer = file.read(buffer_len)

            while (buffer >= '0' and buffer <= '9') and buffer:     # обработка чисел
                position += 1
                if int(buffer) % 2 == 0:
                    for i in range(position):
                        print(int(buffer))
                buffer = file.read(buffer_len)
                break

except FileNotFoundError:
    print("\nФайл не обнаружен.\nДобавьте файл в директорию или переименуйте существующий файл.")

result = time.time() - start                                        
print(" Время работы программы: {:>.10f}".format(result))
