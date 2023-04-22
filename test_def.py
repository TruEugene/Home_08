# Малашкин Артём Сергеевич 3 вариант
import streamlit as st


def t_def():
    st.text('Тест всякого')
    values = st.slider("Задайте диапазон возраста", 0, 120, (30, 60))
    with open("data.csv") as data_file:
        for line in data_file:
            lst = line.split(',')
            pclass = lst[2]
            name = lst[3] + lst[4]
            sex = lst[5]
            age = lst[6]
            if sex == "male" and age != '' and int(age).between(values):
                st.text(name[1:-1] + " " + age + " " + pclass)
