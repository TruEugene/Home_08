import streamlit as st
import pandas as pd


def mariya_def():
    st.header('Данные пассажиров с билетом нулевой стоимости')

    df = pd.read_csv('data.csv', delimiter=',')
    df_nullcost = df[(df['Fare'] == 0)]
    df_nullcost.columns = ['Ид пассажира', 'Спасен (да/нет)', 'Класс каюты', 'ФИО', 'Пол', 'Возраст',
                           'Количество родственников на борту', 'Количество родителей/детей на борту', 'Номер билета',
                           'Плата за проезд', 'Каюта', 'Порт посадки']
    choice = st.radio('Вас интересует список:', ['Спасен', 'Не спасен'])
    if choice == 'Спасен':
        st.dataframe(df_nullcost[(df_nullcost['Спасен (да/нет)'] == 1)])
    else:
        st.dataframe(df_nullcost[(df_nullcost['Спасен (да/нет)'] == 0)])
