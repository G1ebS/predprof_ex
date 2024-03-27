def first_half_checker(stop_hours, stop_minutes, stop_seconds):
    """Функция проверяет в какой половине дня время
    
    stop_hours - часы
    stop_minutes - минуты
    stop_seconds - секунды
    """
    sum_seconds = (stop_hours) * 60 * 60 + (stop_minutes) * 60 + (stop_seconds)
    return sum_seconds >= 0 and sum_seconds <= 12 * 60 * 60

with open("astronaut_time.txt", "r", encoding="utf-8") as input_file: # читаем файл
    data = [line.strip().split(">") for line in input_file.readlines()][1::] # записываем строки(кроме заголовка) в список data, разделяем по данному в условии разделителю
    first_half = list() # список кабин, выключившихся для первого промежутка времени (первая половина дня)
    second_half = list() # список кабин, выключившихся для второго промежутка времени (вторая половина дня)
    for WatchNumber, numberStation, cabinNumber, timeStop, count in data: # идем по кабинам
        stop_hours, stop_minutes, stop_seconds = map(int, timeStop.split(":")) # форматируем время остановки
        if first_half_checker(stop_hours, stop_minutes, stop_seconds): # проверяем в какой половине дня случилась отсановка
            first_half.append([WatchNumber, numberStation, cabinNumber, timeStop, count])
        else:
            second_half.append([WatchNumber, numberStation, cabinNumber, timeStop, count])
    print(f"{len(first_half)} станций остановилось с период с 00.00 до 12.00.")
    print(f"{len(second_half)} станций остановилось с период с 12.01 до 23.59.")