import streamlit as st


def t_def():
    #    st.header("Посчитать долю пассажиров Титаника, указав: вести поиск среди спасенных или погибших")
    with open("data.csv") as file:
        surv30 = 0
        surv60 = 0
        unsurv30 = 0
        unsurv60 = 0
        count = -1
        for line in file:
            data = line.rstrip().split(",")
            count += 1
            if data[1] == "1":
                if data[6] < "30":
                    surv30 += 1
                if data[6] > "60":
                    surv60 += 1
            if data[1] == "0":
                if data[6] < "30":
                    unsurv30 += 1
                if data[6] > "60":
                    unsurv60 += 1

    choice = st.radio("Вести поиск среди:", ["Спасенных", "Погибших"])

    #    st.write(count)

    if choice == "Спасенных":
        st.success("Доля спасенных пассажиров Титаника")
        st.write("Моложе 30: ", round((surv30 / count) * 100, 2), "%",
                 "Старше 60: ", round((surv60 / count) * 100, 2), "%")
    elif choice == "Погибших":
        st.error("Доля погибших пассажиров Титаника")
        st.write("Моложе 30: ", round((unsurv30 / count) * 100, 2), "%",
                 "Старше 60: ", round((unsurv60 / count) * 100, 2), "%")
