import pandas as pd
import sqlite3

pd.set_option('display.max_columns', 15)

# Считывание данных из Excel файла
excel_file_path = 'Проект parsing_exel/ОНПЗ_Булкин Д.В._ППР_Тумаков С.И._январь.xlsx'
header_rows = list(range(9, 13))
start_data_row = 13
df = pd.read_excel(excel_file_path, header=header_rows)

# # Извлечение данных по названиям столбцов
# # Например, если у вас есть столбец "Имя" и "Возраст"
selected_column = [
    'Технологическая установка (объект), место установки',
    'Тип электрооборудования / марка электроборудования',
    'ФИО исполнителя работ / № акта переноса'
]
values_column = df[selected_column].dropna()

# Вывод значений столбца
print(f'Значения столбцов "{selected_column}":\n{values_column}')

# print(df)

# # Подключение к базе данных SQLite
# db_path = 'путь_к_вашей_базе_данных.db'
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()
#
# # Создание таблицы в базе данных (если она ещё не существует)
# table_name = 'ваша_таблица'
# df.to_sql(table_name, conn, index=False, if_exists='replace')
#
# # Закрытие соединения с базой данных
# conn.close()
