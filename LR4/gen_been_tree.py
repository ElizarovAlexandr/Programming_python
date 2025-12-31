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
