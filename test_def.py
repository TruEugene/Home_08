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

    # Удалим ненужные столбцы из отфильтрованной таблицы.
    save_male = pd.DataFrame(data=save_male, columns=columns)

    # Вывести Pclass, Name, Age спасённых с именами начинающихся на введённый текст
    values = st.slider("Задайте диапазон возраста", 0, 120, (30, 60))

    age = save_male['Age']

    if age != '':
        st.write(save_male[save_male['Age'].between(values)])
