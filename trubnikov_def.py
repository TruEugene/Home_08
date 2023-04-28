import streamlit as st
import pandas as pd


def eugene_def():
    # Загрузка и запись файла в переменную
    df = pd.read_csv('data.csv')

    # Создадим переменную saved и запишем в неё отфильтрованную таблицу
    saved = df[df['Survived'] == 1]

    # Выберем нужные столбцы для отображения
    columns = ['Pclass', 'Name', 'Age']

    # Удалим ненужные столбцы из отфильтрованной таблицы.
    saved = pd.DataFrame(data=saved, columns=columns)

    st.header("Поиск пассажиров Титаника")

    # Вывести Pclass, Name, Age спасённых с именами начинающихся на введённый текст
    name = st.text_input("Введите первые буквы фамилии")
    st.write(saved[saved['Name'].str.startswith(name)])

