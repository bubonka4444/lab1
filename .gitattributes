""""Вариант 1.
Написать программу, которая читая последовательность цифр из файла, вводит на экран четные цифры, стоящие на нечетных местах,
 повторяя каждую цифру так, чтобы число повторов равнялось номеру позиции цифры.
"""

import time

start = time.time()                                                 # начинаем отсчет

buffer_len = 1                                                      # размер буфера чтения
position = 0                                                        # номер позиции цифры

try:
    with open("prikol.txt", "r") as file:                           # открываем файлик
        buffer = file.read(buffer_len)

        while buffer:                                               # пока в файлике что-то есть
            while (buffer < '0' or buffer > '9') and buffer:        # пока это циферка
                buffer = file.read(buffer_len)

            while (buffer >= '0' and buffer <= '9') and buffer:     # обработка циферок
                position += 1
                if int(buffer) % 2 == 0:
                    for i in range(position):
                        print(int(buffer))
                buffer = file.read(buffer_len)
                break

except FileNotFoundError:
    print("\nФайл не обнаружен.\nДобавьте файл в директорию или переименуйте существующий файл.")

result = time.time() - start                                        # заканчиваем отсчет
print(" Время работы программы: {:>.10f}".format(result))
