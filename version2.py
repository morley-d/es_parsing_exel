# deprecated file

import pandas as pd
import sqlite3
import os

# Путь к папке с Excel файлами
folder_path = './Проект parsing_exel'

# Подключение к базе данных SQLite
db_path = 'task_base.db'
conn = sqlite3.connect(db_path)

# Название таблицы в базе данных
table_name = 'task'

# Цикл по всем Excel файлам в папке
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx'):
        file_path = os.path.join(folder_path, file_name)

        # Загрузка данных из Excel файла
        excess_header_rows = list(range(10, 13))
        df = pd.read_excel(file_path, header=9, skiprows=excess_header_rows)

        num_used_rows = int(df['№ п/п'].count() - 3)

        selected_column = [
            'Технологическая установка (объект), место установки',
            'Диспетчерское (технологическое) наименование электрооборудования',
            'Заказчик',
            'ТР',
            'Тип электрооборудования / марка электроборудования',
            'Вид и дата выполнения ',
            'ФИО исполнителя работ / № акта переноса'
        ]
        data = df[selected_column].head(num_used_rows)
        data['status'] = [False] * num_used_rows

        # Сохранение DataFrame в базу данных
        data.to_sql(table_name, conn, index=False, if_exists='append')

# Закрытие соединения с базой данных
conn.close()
