import pandas as pd
import streamlit as st
from malashkin_def import artem_def

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
        assert (data['Sex'] == 'male').all()  # Все строки - мужского пола

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
