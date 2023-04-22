import streamlit as st
import parhacheva_def
import test_def
import trubnikov_def
import fatkieva_def
import malashkin_def
import maslova_def
import urin_def
import cherbadji_def

st.image('https://proprikol.ru/wp-content/uploads/2021/05/kartinki-titanik-44.jpg')

st.title('Проект "Титаник"')

eugene = "Трубников Е.А. (trubnikov.e). Вариант 5."
mariya = "Пархачёва М.А. (masha). Вариант 7."
venera = "Фаткиева В.И. (iris20200). Вариант ."
artem = "Малашкин А.С. (strug2012). Вариант 3."
olga = "Маслова О.И. (o.i.maslova). Вариант ."
ilya = "Юрин И.А. (ily-iury). Вариант ."
nadejda = "Чербаджи Н.А. (kaira1986). Вариант ."
test = "тест"

members_list = [eugene, mariya, venera, artem, olga, ilya, nadejda, test]

member = st.radio("Выберите, чью задачу хотите рассмотреть", members_list)

if member == eugene:
    trubnikov_def.eugene_def()
elif member == mariya:
    parhacheva_def.mariya_def()
elif member == venera:
    fatkieva_def.venera_def()
elif member == artem:
    malashkin_def.artem_def()
elif member == olga:
    maslova_def.olga_def()
elif member == ilya:
    urin_def.ilya_def()
elif member == nadejda:
    cherbadji_def.nadejda_def()
elif member == test_def:
    test_def.t_def()
