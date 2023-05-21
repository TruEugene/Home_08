import pandas as pd
import streamlit as st
from malashkin_def import artem_def


def test_data():
    # Создадим тестовый DataFrame с двумя мужчинами,
    # возраст которых находится в диапазоне [30, 60]
    return pd.DataFrame({
        'Name': ['John Smith', 'Michael Brown'],
        'Age': [35, 45],
        'Sex': ['male', 'male'],
        'Pclass': [1, 2]
    })


def filter_male(data):
    return data[data['Sex'] == 'male']


def test_filter_male():
    # Создадим тестовый DataFrame с двумя мужчинами и двумя женщинами
    data = pd.DataFrame({
        'Name': ['John Smith', 'Michael Brown', 'Mary Johnson', 'Emily Davis'],
        'Age': [35, 45, 25, 30],
        'Sex': ['male', 'male', 'female', 'female'],
        'Pclass': [1, 2, 3, 3]
    })

    # Проверим, что фильтрация по мужчинам работает правильно
    filtered_data = filter_male(data)
    assert len(filtered_data) == 2
    assert (filtered_data['Sex'] == 'male').all()


def test_filter_age():
    # Создадим тестовый DataFrame с одним мужчиной и одной женщиной,
    # возраст которых находится в диапазоне [30, 60]
    return pd.DataFrame({
        'Name': ['John Smith', 'Samantha Johnson'],
        'Age': [35, 50],
        'Sex': ['male', 'female'],
        'Pclass': [1, 2]
    })


def test_artem_def():
    # Создаем тестовый DataFrame с данными
    data = pd.DataFrame({
        'Name': ['John Smith', 'Michael Brown', 'Emma Johnson'],
        'Age': [35, 45, 55],
        'Sex': ['male', 'male', 'female'],
        'Pclass': [1, 2, 3]
    })

    # Заглушка для streamlit.write
    def mock_write(data):
        assert len(data) == 2  # Ожидаем 2 строки
        assert (data['Sex'] == 'male').all()

    # Подменяем streamlit.write
    original_write = st.write
    st.write = mock_write

    # Подменяем pd.read_csv
    original_read_csv = pd.read_csv
    pd.read_csv = lambda _: data

    # Вызываем функцию artem_def
    artem_def()

    # Восстанавливаем оригинальные функции
    st.write = original_write
    pd.read_csv = original_read_csv
