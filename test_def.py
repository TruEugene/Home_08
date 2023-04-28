import streamlit as st


def ilya_def():
    st.header("Посчитать долю пассажиров Титаника, указав: вести поиск среди спасенных или погибших")
    with open("data.csv") as file:
        surv30 = 0
        surv60 = 0
        unsurv30 = 0
        unsurv60 = 0
        count = 0
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

    st.write(count)

    if choice == "среди спасенных":
        st.success("Спасенные пассажиры Титаника")
        st.write("Моложе 30: ", surv30, "Старше 60: ", surv60)
    else:
        st.error("Погибшие пассажиры Титаника")
        st.write("Моложе 30: ", unsurv30, "Старше 60: ", unsurv60)