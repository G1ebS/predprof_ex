"""Код для решения задачи 1""" 

with open("astronaut_time.txt", "r", encoding="utf-8") as input_file: # читаем исходный файл
    data = [line.strip().split(">") for line in input_file.readlines()][1::]  # записываем строки(кроме заголовка) в список data, разделяем по данному в условии разделителю

with open("new_time.csv", "w", encoding="utf-8") as output_file: # открываем файл new_time.csv для записи
    print("WatchNumber, numberStation, cabinNumber, timeStop, timeNow", file=output_file) # выводим в файл столбцы
    for watch_number, number_station, cabin_number, time_stop, count in data: # проходимся по элементам списка data
        hours, minutes, seconds = map(int, time_stop.split(":"))
        hours = (hours + int(count)) % 24 # считаем новое время
        new_time = ":".join([str(hours).rjust(2, "0"), str(minutes), str(seconds)]) # оформляем новое время в формате ЧЧ:ММ:CC
        print(", ".join([watch_number, number_station, cabin_number, time_stop, new_time]), file=output_file) # записываем данные в файл
        if cabin_number == "98-OYE":
            print(f"{new_time} - действительное время для каюты: {cabin_number}") # выводим данные для нужной кабины