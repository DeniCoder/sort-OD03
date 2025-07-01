# Функция меню
def menu():
    choice = int(input("Выберите вид сортировки: \n"
                       "1. Пузырьковая сортировка\n"
                       "2. Быстрая сортировка\n"
                       "3. Сортировка выбором\n"
                       "4. Сортировка вставками\n"))
    if choice == 1:
        mas = enter()
        return print(bubble_sort(mas))
    elif choice == 2:
        mas = enter()
        return print(quick_sort(mas))
    elif choice == 3:
        mas = enter()
        return print(selection_sort(mas))
    elif choice == 4:
        mas = enter()
        return print(insert_sort(mas))
    else:
        print("Выбран неверный пункт меню")
        return menu()

# Функция ввода
def enter():
    try:
        mas = input("Введите целые числа через пробел, которые необходимо отсортировать: ").split()
        mas = list(map(int, mas))
    except ValueError:
        print("Введены некорректные данные")
        return enter()
    return mas

# 1. Пузырьковая сортировка
"""Работает путем многократного прохода по массиву, сравнивая соседние элементы
и меняя их местами, если они находятся в неправильном порядке.
Процесс продолжается до тех пор, пока массив не будет отсортирован."""

def bubble_sort(mas):
    n = len(mas)
    for run in range(n-1):
       for i in range(n-1-run):
           if mas[i] > mas[i + 1]:
               mas[i], mas[i + 1] = mas[i + 1], mas[i]
    return mas

# 2. Быстрая сортировка
"""Работает путем разделения массива на две части: часть, которая уже отсортирована,
и часть, которая не отсортирована. Первая часть массива сортируется, а вторая - не сортируется.
После этого сортировка продолжается для обеих частей массива, используя рекурсивный алгоритм."""

def quick_sort(mas):
    if len(mas) <= 1:
        return mas
    pivot = mas[len(mas)//2]
    center = [x for x in mas if x == pivot]
    right = [x for x in mas if x > pivot]
    left = [x for x in mas if x < pivot]
    return quick_sort(left) + center + quick_sort(right)

# 3. Сортировка выбором
"""Работает путем поиска минимального элемента в неотсортированном массиве
и помещения его в начало отсортированного массива."""

def selection_sort(arr):
   # Проходим по всему списку
   for i in range(len(arr)):
       # Предполагаем, что первый элемент в неотсортированной части - это минимальный
       min_index = i
       # Ищем минимальный элемент в оставшейся части списка
       for j in range(i+1, len(arr)):
           if arr[j] < arr[min_index]:
               min_index = j
       # Меняем местами найденный минимальный элемент с первым элементом в неотсортированной части
       arr[i], arr[min_index] = arr[min_index], arr[i]
   return arr

# 4. Сортировка вставками
"""Работает путем последовательного перемещения элементов массива, 
вставляя каждый элемент на его правильное место в уже отсортированной части массива."""

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == '__main__':
    menu()