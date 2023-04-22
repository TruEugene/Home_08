# Малашкин Артём Сергеевич 3 вариант
import streamlit as st
import pandas as pd


def t_def():
    st.text('тестирование')

    #st.header("Список спасённых мужчин среднего возраста от 30 до 60 лет (поля Name, Age, Pclass)")

    # Создадим переменную df и запишем в неё содержимое data.csv
    df = pd.read_csv('data.csv')

    # Создадим переменную save_male и запишем в неё отфильтрованную таблицу по значениям из задания.
    save_male = df[(df['Survived'] == 1) & (df['Sex'] == "male")]

    # Выберем нужные столбцы.
    columns = ['Name', 'Age', 'Pclass']

    # Удалим ненужные столбцы из отфильтрованной таблицы
    save_male = pd.DataFrame(data=save_male, columns=columns)

    # Вывести Pclass, Name, Age спасённых
    x, y = st.slider("Задайте диапазон возраста", 0, 90, (30, 60))
    save_male_filter = save_male[save_male['Age'].between(x, y)]
    st.write(save_male_filter)

    if st.checkbox('Показать список мужчин без указания возраста'):
        st.write(save_male[save_male['Age'].isna()])
