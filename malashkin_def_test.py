import pandas as pd
import pytest

def test_data():
    # Создадим тестовый DataFrame с двумя мужчинами, возраст которых находится в диапазоне [30, 60]
    return pd.DataFrame({'Name': ['John Smith', 'Michael Brown'],
                         'Age': [35, 45],
                         'Sex': ['male', 'male'],
                         'Pclass': [1, 2]})
def filter_male(data):
    return data[data['Sex'] == 'male']


def test_filter_male():
    # Создадим тестовый DataFrame с двумя мужчинами и двумя женщинами
    data = pd.DataFrame({'Name': ['John Smith', 'Michael Brown', 'Mary Johnson', 'Emily Davis'],
                         'Age': [35, 45, 25, 30],
                         'Sex': ['male', 'male', 'female', 'female'],
                         'Pclass': [1, 2, 3, 3]})

    # Проверим, что фильтрация по мужчинам работает правильно
    filtered_data = filter_male(data)
    assert len(filtered_data) == 2
    assert (filtered_data['Sex'] == 'male').all()

def test_data_3():
    # Создадим тестовый DataFrame с одним мужчиной и одной женщиной, возраст которых находится в диапазоне [30, 60]
    return pd.DataFrame({'Name': ['John Smith', 'Samantha Johnson'],
                         'Age': [35, 50],
                         'Sex': ['male', 'female'],
                         'Pclass': [1, 2]})