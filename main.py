import streamlit as st
import pandas as pd
import parhacheva_def
import trubnikov_def
import fatkieva_def
import malashkin_def
import maslova_def
import urin_def
import cherbadji_def

st.image('https://proprikol.ru/wp-content/uploads/2021/05/kartinki-titanik-44.jpg')

st.title('Проект "Титаник"')

eugene = "Трубников Е.А. (trubnikov.e) - вариант 5."
mariya = "Пархачёва М.А. (masha) - вариант 7."
venera = "Фаткиева В.И. (iris20200) - вариант 8."
artem = "Малашкин А.С. (strug2012) - вариант 3."
olga = "Маслова О.И. (o.i.maslova) - вариант ."
ilya = "Юрин И.А. (ily-iury) - вариант 9."
nadejda = "Чербаджи Н.А. (kaira1986) - вариант 8."
test = "тест"

members_list = [eugene, mariya, venera, artem, olga, ilya, nadejda]

member = st.radio("Выберите, чью задачу хотите рассмотреть", members_list)

if member == eugene:
    st.header("Поиск спасённых пассажиров Титаника")
    df = pd.read_csv('data.csv')
    name = st.text_input("Введите первые буквы фамилии")
    out = trubnikov_def.eugene_def(df, name)
    st.write(out)
elif member == mariya:
    parhacheva_def.mariya_def()
elif member == venera:
    fatkieva_def.venera_def()
elif member == artem:
    malashkin_def.artem_def()
elif member == olga:
    maslova_def.olga_def()
elif member == ilya:
    with open("data.csv") as file:
        data = file.readlines()
    if st.checkbox("Спасен?"):
        save = '1'
    else:
        save = '0'
    out = urin_def.ilya_def(data, save)
    st.write(out)
elif member == nadejda:
    cherbadji_def.nadejda_def()
