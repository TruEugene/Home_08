import streamlit as st
import pandas as pd


def pass_list(data, save):
    data_fare = data[(data['Плата за проезд'] == 0)]
    out_data = data_fare[(data_fare['Спасен (да/нет)'] == save)]
    return (out_data)


def mariya_def():
    st.header('Данные пассажиров с билетом нулевой стоимости')
    data = pd.read_csv('data.csv', delimiter=',')
    data.columns = ['Ид пассажира', 'Спасен (да/нет)', 'Класс каюты', 'ФИО',
                    'Пол', 'Возраст', 'Количество родственников на борту',
                    'Количество родителей/детей на борту', 'Номер билета',
                    'Плата за проезд', 'Каюта', 'Порт посадки']
    radio = st.radio('Вас интересует список:', ['Спасен', 'Не спасен'])
    if radio == 'Спасен':
        save = 1
    else:
        save = 0
    st.dataframe(pass_list(data, save))
