''' Задание 3
Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
- возврат строки без изменений
- возврат строки с преобразованием регистра без потери символов
- возврат строки с удалением знаков пунктуации
- возврат строки с удалением букв других алфавитов
- возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)'''


import string
import unittest


def remove_chars(text: str) -> str:
    abc = string.ascii_letters + ' '
    out_text = ''
    for char in text:
        if char in abc:
           out_text += ''.join(char)        
    return out_text.lower()


class TestRemoveChars(unittest.TestCase):
    def test_remove_chars_no_change(self):
        self.assertEqual(remove_chars('dddddd dddd'), 'dddddd dddd')

    def test_remove_chars_lower(self):
        self.assertEqual(remove_chars('AAA AA'), 'aaa aa')

    def test_remove_chars_remove_chars(self):
        self.assertEqual(remove_chars('a,a,n: v.v;'), 'aan vv')

    def test_remove_chars_remove_rus_alpha(self):
        self.assertEqual(remove_chars('БВАОПоаоваов'), '')

    def test_remove_chars_remove_all(self):
        self.assertEqual(remove_chars('WWW,3322,ГГ:'), 'www')


if __name__ == '__main__':
    unittest.main(verbosity=True)
