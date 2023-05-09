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
    st.header("Анализ данных пассажиров Титаника")

    choice = st.radio("Показать статистику среди:", ["Мужчины", "Женщины"])
    saved = st.radio("Показать:", ["Спасенные", "Погибшие"])

    if choice == "Мужчины":
        st.subheader("Статистика по пассажирам мужского пола")
        if saved == "Спасенные":
            male_survived = count_passengers_by_sex_and_status('male', 1)
            st.write("Количество выживших мужчин: ", male_survived)
        if saved == "Погибшие":
            male_not_survived = count_passengers_by_sex_and_status('male', 0)
            st.write("Количество погибших мужчин: ", male_not_survived)
    elif choice == "Женщины":
        st.subheader("Статистика по пассажирам женского пола")
        if saved == "Спасенные":
            female_survived = count_passengers_by_sex_and_status('female', 1)
            st.write("Количество выживших женщин: ", female_survived)
        if saved == "Погибшие":
            female_not_survived = count_passengers_by_sex_and_status('female', 0)
            st.write("Количество погибших женщин: ", female_not_survived)
