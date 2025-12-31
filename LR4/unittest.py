import unittest
from gen_bin_tree import gen_bin_tree


class TestGenBinTree(unittest.TestCase):
    """Тесты для функции gen_bin_tree"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.default_tree = gen_bin_tree()
    
    def test_default_parameters(self):
        """Тест с параметрами по умолчанию"""
        tree = self.default_tree
        
        # Проверяем структуру
        self.assertIsInstance(tree, dict)
        self.assertIn("value", tree)
        self.assertIn("left", tree)
        self.assertIn("right", tree)
        
        # Проверяем значения по умолчанию
        self.assertEqual(tree["value"], 3)  # root=3
        
        # Проверяем левого потомка корня
        self.assertEqual(tree["left"]["value"], 5)  # 3 + 2 = 5
        
        # Проверяем правого потомка корня
        self.assertEqual(tree["right"]["value"], 9)  # 3 * 3 = 9
    
    def test_custom_height(self):
        """Тест с пользовательской высотой"""
        # Высота 1 - только корень
        tree = gen_bin_tree(height=1, root=10)
        self.assertEqual(tree["value"], 10)
        self.assertIsNone(tree["left"])
        self.assertIsNone(tree["right"])
        
        # Высота 2 - корень + два потомка
        tree = gen_bin_tree(height=2, root=10)
        self.assertEqual(tree["value"], 10)
        self.assertEqual(tree["left"]["value"], 12)  # 10 + 2
        self.assertEqual(tree["right"]["value"], 30)  # 10 * 3
        self.assertIsNone(tree["left"]["left"])
        self.assertIsNone(tree["left"]["right"])
        self.assertIsNone(tree["right"]["left"])
        self.assertIsNone(tree["right"]["right"])
    
    def test_custom_root(self):
        """Тест с пользовательским корнем"""
        tree = gen_bin_tree(root=7)
        
        self.assertEqual(tree["value"], 7)
        self.assertEqual(tree["left"]["value"], 9)  # 7 + 2
        self.assertEqual(tree["right"]["value"], 21)  # 7 * 3
    
    def test_custom_functions(self):
        """Тест с пользовательскими функциями для потомков"""
        tree = gen_bin_tree(
            height=3,
            root=5,
            left_leaf=lambda x: x * 2,
            right_leaf=lambda x: x + 5
        )
        
        # Проверяем корень
        self.assertEqual(tree["value"], 5)
        
        # Проверяем первого уровня
        self.assertEqual(tree["left"]["value"], 10)  # 5 * 2
        self.assertEqual(tree["right"]["value"], 10)  # 5 + 5
        
        # Проверяем второго уровня
        self.assertEqual(tree["left"]["left"]["value"], 20)  # 10 * 2
        self.assertEqual(tree["left"]["right"]["value"], 15)  # 10 + 5
        self.assertEqual(tree["right"]["left"]["value"], 20)  # 10 * 2
        self.assertEqual(tree["right"]["right"]["value"], 15)  # 10 + 5
    
    def test_edge_cases(self):
        """Тест крайних случаев"""
        # Высота 0
        self.assertIsNone(gen_bin_tree(height=0))
        
        # Высота отрицательная
        self.assertIsNone(gen_bin_tree(height=-1))
        
        # Отрицательный корень
        tree = gen_bin_tree(height=2, root=-5)
        self.assertEqual(tree["value"], -5)
        self.assertEqual(tree["left"]["value"], -3)  # -5 + 2
        self.assertEqual(tree["right"]["value"], -15)  # -5 * 3
    
    def test_type_validation(self):
        """Тест валидации типов"""
        # Проверка неверного типа для height
        with self.assertRaises(TypeError):
            gen_bin_tree(height="invalid")
        
        # Проверка неверного типа для root
        with self.assertRaises(TypeError):
            gen_bin_tree(root="invalid")
        
        # Проверка неверного типа для left_leaf
        with self.assertRaises(TypeError):
            gen_bin_tree(left_leaf="not a function")
        
        # Проверка неверного типа для right_leaf
        with self.assertRaises(TypeError):
            gen_bin_tree(right_leaf=123)
    
    def test_tree_structure(self):
        """Тест структуры дерева"""
        tree = gen_bin_tree(height=3, root=2)
        
        # Проверяем, что дерево имеет правильную структуру
        self.assertIsInstance(tree, dict)
        self.assertIn("value", tree)
        self.assertIn("left", tree)
        self.assertIn("right", tree)
        
        # Проверяем значения на каждом уровне
        # Уровень 0 (корень)
        self.assertEqual(tree["value"], 2)
        
        # Уровень 1
        self.assertEqual(tree["left"]["value"], 4)  # 2 + 2
        self.assertEqual(tree["right"]["value"], 6)  # 2 * 3
        
        # Уровень 2
        self.assertEqual(tree["left"]["left"]["value"], 6)  # 4 + 2
        self.assertEqual(tree["left"]["right"]["value"], 12)  # 4 * 3
        self.assertEqual(tree["right"]["left"]["value"], 8)  # 6 + 2
        self.assertEqual(tree["right"]["right"]["value"], 18)  # 6 * 3
        
        # Проверяем, что листья имеют None в качестве потомков
        self.assertIsNone(tree["left"]["left"]["left"])
        self.assertIsNone(tree["left"]["left"]["right"])
        self.assertIsNone(tree["left"]["right"]["left"])
        self.assertIsNone(tree["left"]["right"]["right"])
        self.assertIsNone(tree["right"]["left"]["left"])
        self.assertIsNone(tree["right"]["left"]["right"])
        self.assertIsNone(tree["right"]["right"]["left"])
        self.assertIsNone(tree["right"]["right"]["right"])
    
    def test_zero_height(self):
        """Тест с нулевой высотой"""
        result = gen_bin_tree(height=0)
        self.assertIsNone(result)
    
    def test_negative_height(self):
        """Тест с отрицательной высотой"""
        result = gen_bin_tree(height=-5)
        self.assertIsNone(result)
    
    def test_complex_functions(self):
        """Тест со сложными функциями для потомков"""
        tree = gen_bin_tree(
            height=2,
            root=10,
            left_leaf=lambda x: x ** 2,
            right_leaf=lambda x: x // 2
        )
        
        self.assertEqual(tree["value"], 10)
        self.assertEqual(tree["left"]["value"], 100)  # 10 ** 2
        self.assertEqual(tree["right"]["value"], 5)  # 10 // 2


if __name__ == "__main__":
    unittest.main(verbosity=2)
