def ilya_def(data, save):
    #    unsurv60 = 0
    #    unsurv30 = 0
    avg30 = 0
    avg60 = 0
    #    min30 = "Моложе 30 - "
    #    max60 = "Старше 60 - "
    #   with open("data.csv") as file:
    for line in data:
        survived = line.rstrip().split(",")
        if line.split(",")[0] == "PassengerId":
            continue
        if int(survived[1]) == int(save):
            if survived[6] < "30":
                avg30 += 1
            if survived[6] > "60":
                avg60 += 1
            # if survived[1] == "0":
            #   if survived[6] < "30":
            #      unsurv30 += 1
            # if survived[6] > "60":
            #    unsurv60 += 1
        # choice = st.radio ("Среди кого вести поиск?", ["среди спасенных", "среди погибших"])
        # if choice == "среди спасенных":
        #   st.success("Спасенные пассажиры Титаника")
        avg1 = (str(avg30) + ", ")
        avg2 = (str(avg60))
        avg = avg1 + avg2
    return avg
    # st.text(avg)
    # st.warning("Погибшие пассажиры Титаника")
    # uavg1 = (min30 + str(unsurv30) + ", ")
    # uavg2 = (max60 + str(unsurv60))
    #        uavg = uavg1 + uavg2
    #  st.text(uavg)

# with open("data.csv") as file:
#    data = file.readlines()
# print(ilya_def(data, 1))
