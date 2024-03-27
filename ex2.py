"""Код для решения задачи 2"""



def bubble_sort(data: list, key=lambda x: x) -> None:
    """
    Принимает список и ключ, ничего не возвращает, сортирует список по убыванию, 
    в зависимости от значений ключа, возвращаемых 
    при применении его к элементу списка списка. Работает по принципу сортировки пузырьком
    

    data - список для сортировки, тип - list
    key - функция применяемая для сравнения элементов, по умолчанию - lambda x: x
    (функция, которая возвращает аргумент при котором вызвалась, 
    т.е при значении key по умолчанию список сортируется в 
    зависимости от типа данных внутри)
    """
    for i in range(len(data)):
        for j in range(i, len(data)):
            if key(data[i]) > key(data[j]):
                data[i], data[j] = data[j], data[i]

# data = [3, 2, 1, 9, 7, 4]
# bubble_sort(data)
# print(data)
                
with open("new_time.csv", "r", encoding="utf-8") as input_file:
    data = [line.split(", ") for line in input_file.readlines()][1::]
    bubble_sort(data, key=lambda x: x[1])
    for WatchNumber, numberStation, cabinNumber, timeStop, timeNow in data[:3]:
        print(f"На станции {numberStation} в каюте {cabinNumber} восстановлено время. Актуальное время: {timeNow}")

