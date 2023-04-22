import streamlit as st
import pandas as pd

st.subheader("Спасённые женщины Титаника")

def eugene_def():
    # Создадим переменную df и запишем в неё содержимое data.csv
    df = pd.read_csv('data.csv')

    # Вариант 5: записать в файл saveFem.txt данные спасенных женщин (поля Pclass, Name, Age).

    # Создадим переменную save_fem и запишем в неё отфильтрованную таблицу по значениям из задания.
    save_fem = df[(df['Survived'] == 1) & (df['Sex'] == "female")]

    # Выберем нужные столбцы.
    columns = ['Pclass', 'Name', 'Age']

    # Удалим ненужные столбцы из отфильтрованной таблицы.
    save_fem = pd.DataFrame(data=save_fem, columns=columns)

    # Возможность показать df из 5 ЛР
    if st.checkbox('Показать список'):
        st.write(save_fem)

    # Вывести Pclass, Name, Age спасённых с именами начинающихся на введённый текст
    name = st.text_input("Поиск по начальным буквам имени?")
    if name != '':
        st.write(
            save_fem[save_fem['Name'].str.startswith(name)]
        )
