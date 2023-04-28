import streamlit as st
import pandas as pd

def venera_def():
        # Загрузка данных о пассажирах "Титаника"
    data = pd.read_csv('data.csv')

    # Определение функции для подсчета количества пассажиров по полу и статусу (спасенные/погибшие)
    def count_passengers_by_sex_and_status(sex, status):
        filtered_data = data[(data['Sex'] == sex) & (data['Survived'] == status)]
        count = filtered_data.shape[0]
        return count

    # Заголовок и описание веб-приложения
    st.title("Анализ данных пассажиров Титаника")

    # Вывод статистики по количеству пассажиров мужского пола
    st.subheader("Статистика по мужским пассажирам")
    male_survived = count_passengers_by_sex_and_status('male', 1)
    male_not_survived = count_passengers_by_sex_and_status('male', 0)
    st.write("Количество выживших мужчин: ", male_survived)
    st.write("Количество погибших мужчин: ", male_not_survived)

    # Вывод статистики по количеству пассажиров женского пола
    st.subheader("Статистика по женским пассажирам")
    female_survived = count_passengers_by_sex_and_status('female', 1)
    female_not_survived = count_passengers_by_sex_and_status('female', 0)
    st.write("Количество выживших женщин: ", female_survived)
    st.write("Количество погибших женщин: ", female_not_survived)
