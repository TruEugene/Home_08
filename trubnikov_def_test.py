import pandas as pd
from trubnikov_def import eugene_def


def test_eugene_def(monkeypatch):
    # Создаем тестовый DataFrame
    data = pd.DataFrame({
        'Survived': [1, 0, 1],
        'Pclass': [1, 2, 3],
        'Name': ['Eugene', 'John', 'Jane'],
        'Age': [20, 30, 40]
    })

    # Функция-заглушка для ввода текста от пользователя
    def mock_input(prompt):
        return 'E'

    # Замена встроенной функции input() на функцию-заглушку
    monkeypatch.setattr('builtins.input', mock_input)

    # Вызов функции eugene_def с тестовыми данными
    result = eugene_def(data, 'E')

    # Ожидаемый результат
    expected_result = pd.DataFrame({
        'Pclass': [1],
        'Name': ['Eugene'],
        'Age': [20]
    })

    # Проверка результатов
    pd.testing.assert_frame_equal(result, expected_result)

