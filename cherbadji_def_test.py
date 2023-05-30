import unittest
import pandas as pd
from cherbadji_def import filtred

data = {'Sex': ['male', 'female', 'male', 'male', 'female', 'female'],
        'Survived': [1, 1, 0, 1, 0, 1]}
df = pd.DataFrame(data)


class TestFiltred(unittest.TestCase):
    def test_filtred(self):
        # Проверяем результаты для спасенных мужчин
        result = filtred(df, 'male', 1)
        expected_result = 2
        self.assertEqual(result, expected_result)

        # Проверяем результаты для спасенных женщин
        result = filtred(df, 'female', 1)
        expected_result = 2
        self.assertEqual(result, expected_result)

        # Проверяем результаты для погибших мужчин
        result = filtred(df, 'male', 0)
        expected_result = 1
        self.assertEqual(result, expected_result)

        # Проверяем результаты для погибших женщин
        result = filtred(df, 'female', 0)
        expected_result = 1
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
