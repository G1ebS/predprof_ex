with open("astronaut_time.txt", "r", encoding="utf-8") as input_file: # читаем файл
    data = [line.strip().split(">") for line in input_file.readlines()][1::] # записываем строки(кроме заголовка) в список data, разделяем по данному в условии разделителю
    d = dict() # создаем хэш таблицу
    for WatchNumber, numberStation, cabinNumber, timeStop, count in data:
        hours, minutes, seconds = timeStop.split(":")
        hours = str((int(hours) + int(count)) % 24).rjust(2, "0")
        timeNow = ":".join([hours, minutes, seconds])
        d[cabinNumber] = {"WatchNumber": WatchNumber, "numberStation": numberStation, "timeStop": timeStop, "Count": count, "timeNow": timeNow} # заносим данные
    for key in list(d.keys())[:10]: # выводим данные о первыч 10
        print(f"Номер каюты: {key}; Информация о каюте: {d[key]}") 