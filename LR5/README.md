### Лабораторная работа 5. Сравнение функций. Мемоизация

## Формулировка задания:
Сравните время работы двух реализаций функции вычисления факториала:

рекурсивной,

нерекурсивной (через цикл).

Изучить материал про мемоизацию и реализовать сравнение мемоизованных и немемоизованных вариантов функций (рекурсивной и нерекурсивной. Проанализировать результаты и сделать выводы, описать выводы в отчете, построить графики.

Для сравнения используйте модуль timeit, а для наглядности постройте график с помощью matplotlib, показывающий зависимость времени выполнения от входных данных.


Условия:

Реализуйте две функции fact_recursive(n) и fact_iterative(n).

Для корректного сравнения используйте одинаковый набор чисел для тестирования.

Визуализируйте результаты (ось X — размер входного числа n, ось Y — время вычислений).

Сравните эффективность двух подходов.



# Декоратор для кэширования результатов функции
```python
from typing import Callable

def cache(func: Callable):
    cache = {}
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        result = func(*args, **kwargs)
        cache[args] = result
        return result
    return wrapper
Итеративный факториал
python
from cache import cache

def factorial_iterative(n):
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

```

# Рекурсивный факториал
```python
from cache import cache

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

```

# Сравнение времени выполнения функций факториала
```python
import timeit
import matplotlib.pyplot as plt
from factorial_iterative import factorial_iterative
from factorial_recursive import factorial_recursive

def benchmark(func, data, number=1, repeat=5):
    total = 0
    for n in data:
        times = timeit.repeat(lambda: func(n), number=number, repeat=repeat)
        total += min(times)
    return total / len(data)

def main():
    test_data = list(range(10, 300, 10))

    res_recursive = []
    res_iterative = []

    for n in test_data:
        res_recursive.append(benchmark(factorial_recursive, [n], number=10000, repeat=5))
        res_iterative.append(benchmark(factorial_iterative, [n], number=10000, repeat=5))

    plt.plot(test_data, res_recursive, label="Рекурсивный")
    plt.plot(test_data, res_iterative, label="Итеративный")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение рекурсивного и итеративного факториала без кэширования")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

```

# Графики

![](Figure_1.png)
![](Figure_2.png)

Вывод
Ожидаемо, результаты вычислений с использованием кэширования (мемоизации) оказались значительно быстрее по сравнению с вариантами без кэширования. На графике с мемоизацией наблюдаются незначительные скачки времени выполнения — они, вероятнее всего, связаны с фоновыми процессами операционной системы, а не с ошибками в коде. В целом, мемоизация существенно повышает эффективность функций, требующих высоких вычистельных мощностей, и снижает нагрузку на процессор.Лабораторная работа 5. Сравнение функций. Мемоизация
