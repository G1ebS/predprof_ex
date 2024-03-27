"""Код для решения задачи 3""" 

with open("astronaut_time.txt", "r", encoding="utf-8") as input_file: # читаем исходный файл
    data = [line.strip().split(">") for line in input_file.readlines()][1::] # записываем строки(кроме заголовка) в список data, разделяем по данному в условии разделителю

while True:
    cabin_number = input() # читаем из консоли номер кабины
    if cabin_number == "none":
        break
    for WatchNumber, numberStation, cabinNumber, timeStop, count in data: # Ищем кабину с таким номером
        if cabinNumber == cabin_number:
            hours, minutes, seconds = timeStop.split(":") # считаем новое время
            hours = str((int(hours) + int(count)) % 24).rjust(2, "0") # форматируем время
            timeNow = ":".join([hours, minutes, seconds])
            print(f"В каюте {cabinNumber} восстановлено время (время остановки: {timeStop}). Актуальное время: {timeNow}") # Выводим ответ