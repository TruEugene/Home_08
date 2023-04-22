import streamlit as st
import pandas as pd

def eugene_def():
    st.header("Спасённые пассажиры Титаника")

    # Создадим переменную df и запишем в неё содержимое data.csv
    df = pd.read_csv('data.csv')

    # Вариант 5: данные всех спасённых (поля Pclass, Name, Age).

    # Создадим переменную saved и запишем в неё отфильтрованную таблицу по значению из задания.
    saved = df[df['Survived'] == 1]

    # Выберем нужные столбцы.
    columns = ['Pclass', 'Name', 'Age']

    # Удалим ненужные столбцы из отфильтрованной таблицы.
    saved = pd.DataFrame(data=saved, columns=columns)

    # Возможность показать всю таблицу
    if st.checkbox('Показать весь список выживших'):
        st.write(saved)

    # Вывести Pclass, Name, Age спасённых с именами начинающихся на введённый текст
    name = st.text_input("Поиск по начальным буквам имени:")
    if name != '':
        st.write(saved[saved['Name'].str.startswith(name)])
