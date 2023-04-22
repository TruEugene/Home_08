#Малашкин Артём Сергеевич 3 вариант
import streamlit as st
st.text('Список пассажиров Титаника!')
age = st.slider ('Сколько лет пассажирам титаника мужского пола от 30 до 60 лет', 30, 60, 35)
with open("data.csv") as data_file:
    for line in data_file:
        lst = line.split(',')
        pclass = lst[2]
        name = lst[3] + lst[4]
        sex = lst[5]
        age = lst[6]
        if sex == "male" and age != '' and float(age) >= 30 and float(age) <= 60:
            st.text(name[1:-1] + " "+ age + " " + pclass)