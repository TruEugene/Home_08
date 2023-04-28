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

    choice = st.radio("Среди кого вести поиск?", ["среди спасенных", "среди погибших"])

#    st.write(count)

    if choice == "среди спасенных":
        st.success("Доля спасенных пассажиров Титаника")
        st.write("Моложе 30: ", surv30/count, "Старше 60: ", surv60/count)
    else:
        st.error("Доля погибших пассажиров Титаника")
        st.write("Моложе 30: ", unsurv30/count, "Старше 60: ", unsurv60/count)