# ЛР 2 — Задача «Сумма двух» (Two Sum)

## Формулировка задания

Дан массив целых чисел nums и целочисленное значение переменной target , верните индексы двух чисел таким образом, чтобы они в сумме давали target. У каждого входного набора может не быть решений и может быть только одно решение, если есть элементы дающие в сумме target. Вы не можете  использовать один и тот же элемент дважды (и соответственно индекс тоже). Вы можете вернуть ответ в любом порядке нахождения индексов.
Условия:

### Примеры

**Example 1**  
Input: `nums = [2,7,11,15]`, `target = 9`  
Output: `[0,1]`

**Example 2**  
Input: `nums = [3,2,4]`, `target = 6`  
Output: `[1,2]`

**Example 3**  
Input: `nums = [3,3]`, `target = 6`  
Output: `[0,1]`

---

## Реализация

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []
```

---

### Тесты
```import unittest
from two_sum import two_sum


class TestTwoSum(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_example_2(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_example_3(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
```
Запуск тестов
bash
python test_two_sum.py
При использовании Google Colab тесты запускаются корректно благодаря параметрам:

argv=[''], exit=False
```
