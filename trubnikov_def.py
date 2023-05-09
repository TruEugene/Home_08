import streamlit as st
import pandas as pd

df = pd.read_csv('data.csv')


def eugene_def(data, n):
    # Создадим переменную saved и запишем в неё отфильтрованную таблицу
    saved = data[data['Survived'] == 1]

    # Выберем нужные столбцы для отображения
    columns = ['Pclass', 'Name', 'Age']

    # Удалим ненужные столбцы из отфильтрованной таблицы.
    saved = pd.DataFrame(data=saved, columns=columns)

    # Вывести Pclass, Name, Age спасённых с именами начинающихся на введённый текст
    out = saved[saved['Name'].str.startswith(n)]
    return out


st.header("Поиск спасённых пассажиров Титаника")
name = st.text_input("Введите первые буквы фамилии")
st.write(eugene_def(df, name))
