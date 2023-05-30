import streamlit as st
import pandas as pd

df = pd.read_csv('data.csv')


def filtred(data, sex, save):
    filtered_data = data[(data['Sex'] == sex) & (data['Survived'] == save)]
    count = filtered_data.shape[0]
    return count


def nadejda_def():
    st.header("Подсчёт количества пассажиров (выбрав пол, и спасенных или погибших)")

    if st.checkbox("Спасен?"):
        save = '1'
    else:
        save = '0'

    if save == '1':
        m_surv = filtred(df, 'male', 1)
        f_surv = filtred(df, 'female', 1)
        st.text(f'Количество спасенных мужчин {m_surv}')
        st.text(f'Количество спасенных женщин {f_surv}')
    else:
        m_not_surv = filtred(df, 'male', 0)
        f_not_surv = filtred(df, 'female', 0)
        st.text(f'Количество погибших мужчин {m_not_surv}')
        st.text(f'Количество погибших женщин {f_not_surv}')
