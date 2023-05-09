import pandas as pd
from main import eugene_def


def test_eugene_def():
    # Создаем тестовый файл data.csv
    data = pd.DataFrame({
        'Survived': [1, 0, 0],
        'Pclass': [1, 2, 3],
        'Name': ['Trubnikov', 'John', 'Trujennikov'],
        'Age': [20, 30, 40]
    })
    data.to_csv('data.csv', index=False)

    # Вызов функции eugene_def с тестовыми данными
    result = eugene_def('Tr')

    # Ожидаемый результат
    expected_result = pd.DataFrame({
        'Pclass': [1],
        'Name': ['Trubnikov'],
        'Age': [20]
    })

    # Проверка результатов
    pd.testing.assert_frame_equal(result, expected_result)
