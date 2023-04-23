import streamlit as st
import pandas as pd


def malashkin_def():
    st.text('Вывод данных')

    st.header("Список  мужчин среднего возраста от 30 до 60 лет (поля Name, Age, Pclass)")

    # Создадим переменную df и запишем в неё содержимое data.csv
    df = pd.read_csv('data.csv')

    # Создадим переменную male и запишем в неё отфильтрованную таблицу по значениям из задания.
    male = df[df['Sex'] == "male"]

    # Выберем нужные столбцы.
    columns = ['Name', 'Age', 'Pclass']

    # Удалим ненужные столбцы из отфильтрованной таблицы
    male = pd.DataFrame(data=male, columns=columns)

    # Вывести Pclass, Name, Age мужчин
    x, y = st.slider("Задайте диапазон возраста", 0, 90, (30, 60))
    male_filter = male[male['Age'].between(x, y)]
    st.write(male_filter)

    if st.checkbox('Показать список мужчин без указания возраста'):
        st.write(male[male['Age'].isna()])