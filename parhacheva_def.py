import streamlit as st

def pass_list(data, save):
    titanic = []
    for line in data:
        if line.split(',')[10] != "" and line.split(',')[10] == "0" and line.split(',')[1] == save:
            titanic += [line]
    return (titanic)

def mariya_def():
    with open("data.csv") as data_file:
        data = data_file.readlines()[1:]
    st.title('Список пассажиров Титаника с нулевой стоимостью билета')
    radio = st.radio("Спасен?", ['Да', 'Нет'])
    if radio == 'Да':
        save = '1'
    else:
        save = '0'
    st.dataframe(pass_list(data, save))

