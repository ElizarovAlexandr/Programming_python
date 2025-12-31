# Лабораторная работа №4

## Тема: Нерекурсивная генерация бинарного дерева
### Формулировка задания:
Напишите на языке Python нерекурсивную функцию gen_bin_tree, которая будет строить бинарное дерево.

Алгоритм построения дерева должен учитывать параметры height, root, left_leaf и right_leaf, переданные в качестве аргументов функции.

Если для указанных параметров были переданы значения, то используются они.
В противном случае должны использоваться значения, указанные в варианте.
Базовый вариант решения задачи должен представлять результат в виде словаря с ключами value, left, right.

Построенное дерево должно обладать следующими свойствами:

В корне дерева (root) находится число, которое задает пользователь.
Высота дерева (height) задается пользователем.
Левый (left) и правый потомок (right) вычисляется с использованием алгоритмов (left_leaf и right_leaf).
Алгоритмы по умолчанию нужно задать с использованием lambda-функций.

Далее - исследовать другие структуры, в том числе доступные в модуле collections в качестве контейнеров для хранения структуры бинарного дерева. 

### Основной модуль

```python
from collections import deque
from typing import Callable, Dict, Any, Optional


def gen_bin_tree(height: int = 4, root: int = 3, 
                 left_leaf: Optional[Callable[[int], int]] = None, 
                 right_leaf: Optional[Callable[[int], int]] = None) -> Optional[Dict[str, Any]]:

    # Проверка типов параметров
    if not isinstance(height, int):
        raise TypeError()
    if not isinstance(root, int):
        raise TypeError()

    if left_leaf is None:
        left_leaf = lambda x: x + 2
    if right_leaf is None:
        right_leaf = lambda x: x * 3

    if not callable(left_leaf):
        raise TypeError()
    if not callable(right_leaf):
        raise TypeError()

    if height <= 0:
        return None

    tree = {"value": root, "left": None, "right": None}

    if height == 1:
        return tree
    
    stack = deque()
    stack.append((tree, root, 1))
    
    while stack:
        current_node, current_value, current_depth = stack.pop()
        if current_depth >= height:
            continue

        left_value = left_leaf(current_value)
        
        if current_depth < height - 1:
            left_node = {"value": left_value, "left": None, "right": None}
            current_node["left"] = left_node
            stack.append((left_node, left_value, current_depth + 1))
        else:
            current_node["left"] = {"value": left_value, "left": None, "right": None}
        right_value = right_leaf(current_value)
        
        if current_depth < height - 1:
            right_node = {"value": right_value, "left": None, "right": None}
            current_node["right"] = right_node
            stack.append((right_node, right_value, current_depth + 1))
        else:
            current_node["right"] = {"value": right_value, "left": None, "right": None}
    
    return tree


if __name__ == "__main__":
    from pprint import pprint
    
    print("Дерево с параметрами по умолчанию:")
    tree = gen_bin_tree()
    pprint(tree)
    
    print("\n\nДерево с пользовательскими параметрами:")
    tree2 = gen_bin_tree(
        height=3,
        root=5,
        left_leaf=lambda x: x - 1,
        right_leaf=lambda x: x + 10
    )
    pprint(tree2)

```
### Тесты
```
Тест со сложными функциями для потомков ... ok
test_custom_functions (__main__.TestGenBinTree.test_custom_functions)
Тест с пользовательскими функциями для потомков ... ok
test_custom_height (__main__.TestGenBinTree.test_custom_height)
Тест с пользовательской высотой ... ok
test_custom_root (__main__.TestGenBinTree.test_custom_root)
Тест с пользовательским корнем ... ok
test_default_parameters (__main__.TestGenBinTree.test_default_parameters)
Тест с параметрами по умолчанию ... ok
test_edge_cases (__main__.TestGenBinTree.test_edge_cases)
Тест крайних случаев ... ok
test_negative_height (__main__.TestGenBinTree.test_negative_height)
Тест с отрицательной высотой ... ok
test_tree_structure (__main__.TestGenBinTree.test_tree_structure)
Тест структуры дерева ... ok
test_type_validation (__main__.TestGenBinTree.test_type_validation)
Тест валидации типов ... ok
test_zero_height (__main__.TestGenBinTree.test_zero_height)
Тест с нулевой высотой ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.002s

OK
```
