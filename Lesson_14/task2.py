# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import unittest

from task1 import del_not_ascii


class TestTask1(unittest.TestCase):

    def test_not_change(self):
        self.assertEqual(del_not_ascii('HelloWorld'), 'HelloWorld',
                         'Text change!!')

    def test_del_punkt(self):
        self.assertEqual(del_not_ascii('Hello, World!!'), 'HelloWorld',
                         'Text have punkts')

    def test_not_ascii(self):
        self.assertEqual(del_not_ascii('Привет Мир'), '',
                         'Text have ascii')


if __name__ == "__main__":
    unittest.main(verbosity=2)
