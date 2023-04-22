# Малашкин Артём Сергеевич 3 вариант
import streamlit as st
import pandas as pd


def t_def():
    st.text('Тест всякого')

    #    st.header("Спасённые мужчины Титаника среднего возраста")

    # Создадим переменную df и запишем в неё содержимое data.csv
    df = pd.read_csv('data.csv')

    # Вариант 3: список спасённых мужчин среднего возраста от 30 до 60 лет (поля Name, Age, Pclass).

    # Создадим переменную save_fem и запишем в неё отфильтрованную таблицу по значениям из задания.
    save_male = df[(df['Survived'] == 1) & (df['Sex'] == "male")]

    # Выберем нужные столбцы.
    columns = ['Name', 'Age', 'Pclass']

    # Удалим ненужные столбцы из отфильтрованной таблицы, а также заполним пропуски нулями
    save_male = pd.DataFrame(data=save_male, columns=columns)
    save_male['Age'] = save_male['Age'].fillna(0)

    # Вывести Pclass, Name, Age спасённых
    values = st.slider("Задайте диапазон возраста", 0, 120, (30, 60))
    st.write(values)
    save_male_group = save_male[save_male['Age'].between(values)]
    st.write(save_male_group)


"""
    day_date = st.slider("Date to chose", 0, 120, (30, 60))
    st.write(f"Data for {day_date.date()}")
    df = df[(df['date'] == day_date)]
"""
