import pandas as pd



def eugene_def(data, n):
    # Создадим переменную saved и запишем в неё отфильтрованную таблицу
    saved = data[data['Survived'] == 1]

    # Выберем нужные столбцы для отображения
    columns = ['Pclass', 'Name', 'Age']

    # Удалим ненужные столбцы из отфильтрованной таблицы.
    saved = pd.DataFrame(data=saved, columns=columns)

    # Вывести Pclass, Name, Age спасённых с именами начинающихся на введённый текст
    out = saved[saved['Name'].str.startswith(n)]
    return out

