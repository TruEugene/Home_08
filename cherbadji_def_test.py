import unittest
from io import StringIO
from contextlib import redirect_stdout
from cherbadji_def import nadejda_def


class TestNadejdaDef(unittest.TestCase):
    def test_nadejda_def(self):
        data = [
            '100,1,male',
            '120,1,female',
            '140,0,male',
            '160,1,male',
            '180,0,female',
            '200,1,female'
        ]

        expected_output = 3

        # Заменяем стандартный вывод на StringIO для перехвата результатов
        with redirect_stdout(StringIO()) as stdout:
            nadejda_def(data)

            # Получаем результаты из перехваченного вывода
            output = stdout.getvalue().strip()

        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
