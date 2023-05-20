import pandas as pd
from trubnikov_def import eugene_def


def test_eugene_def(monkeypatch):
    # Создаем тестовый DataFrame
    data = pd.DataFrame({
        'Survived': [1, 1, 0],
        'Pclass': [1, 2, 3],
        'Name': ['Trubnikov', 'Ivanov', 'Truschin'],
        'Age': [20, 30, 40]
    })

    # Функция-заглушка для ввода текста от пользователя
    def mock_input(prompt):
        return 'Tr'

    # Замена встроенной функции input() на функцию-заглушку
    monkeypatch.setattr('builtins.input', mock_input)

    # Вызов функции eugene_def с тестовыми данными
    result = eugene_def(data, 'Tr')

    # Ожидаемый результат
    expected_result = pd.DataFrame({
        'Pclass': [1],
        'Name': ['Trubnikov'],
        'Age': [20]
    })

    # Проверка результатов
    pd.testing.assert_frame_equal(result, expected_result)
