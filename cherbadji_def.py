import streamlit as st
import csv


with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    male_survived = 0
    male_died = 0
    female_survived = 0
    female_died = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            if row[4] == 'male':
                if row[1] == '1':
                    male_survived += 1
                elif row[1] == '0':
                    male_died += 1
            elif row[4] == 'female':
                if row[1] == '1':
                    female_survived += 1
                elif row[1] == '0':
                    female_died += 1
    st.text(f'Male passengers survived: {male_survived}')
    st.text(f'Male passengers died: {male_died}')
    st.text(f'Female passengers survived: {female_survived}')
    st.text(f'Female passengers died: {female_died}')
