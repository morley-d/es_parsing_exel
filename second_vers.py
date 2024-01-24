import pandas as pd
import sqlite3

pd.set_option('display.max_columns', 15)

# Путь к Excel файлу
excel_file_path = 'Проект parsing_exel/ОНПЗ_Булкин Д.В._ППР_Тумаков С.И._январь.xlsx'

# Загрузка данных из Excel файла
header_rows = list(range(9, 13))
start_data_row = 13
df = pd.read_excel(excel_file_path, header=header_rows)

# Выбор определенных столбцов
selected_columns_index = [17, 22, 24, 25]
df_selected = df.iloc[:, selected_columns_index]

# Определенное количество строк (например, первые 100 строк)
num_rows = 10
df_selected = df_selected.head(num_rows)

print(df_selected)

# # Подключение к базе данных SQLite
# db_path = 'путь_к_вашей_базе_данных.db'
# conn = sqlite3.connect(db_path)
#
# # Сохранение DataFrame в базу данных
# table_name = 'ваша_таблица'
# df_selected.to_sql(table_name, conn, index=False, if_exists='replace')
#
# # Закрытие соединения с базой данных
# conn.close()