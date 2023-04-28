import streamlit as st


def ilya_def():
    st.header("Посчитать долю пассажиров Титаника, указав: вести поиск среди спасенных или погибших")
    with open("data.csv") as file:
        avg30 = 0
        avg60 = 0
        for line in file:
            survived = line.rstrip().split(",")
            if survived[1] == "1":
                if survived[6] < "30":
                    avg30 += 1
                    if survived[6] > "60":
                        avg60 += 1

                        unsurv30 = 0
                        unsurv60 = 0
                        for line in file:
                            unsurvived = line.rstrip().split(",")
                            if unsurvived[1] == "0":
                                if unsurvived[6] < "30":
                                    unsurv30 += 1
    choice = st.radio("Среди кого вести поиск?", ["среди спасенных", "среди погибших"])
    if choice == "среди спасенных":
        st.success("Спасенные пассажиры Титаника")
        print("моложе 30", avg30, "старше 60 ", avg60)
    else:
        st.warning("Погибшие пассажиры Титаника")
        print("моложе 30", unsurv30, "старше 60", unsurv60)
