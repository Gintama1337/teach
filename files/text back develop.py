import pandas as pd
import openpyxl
import psycopg2
import numpy as np

excel_file = pd.read_excel(r'C:\Users\BeBa\Downloads\Telegram Desktop\1.xlsx', header=[0, 1, 2], sheet_name='Лист1')
excel_read_file = dict(excel_file.to_dict())

table_name_us = 'users'


class Refract:

    def __init__(self):
        self.new_dict = {}

    def create_a_table_dict(self, excel_read_file: dict):
        """
        Редактируем преобразованный в словарь таблицу для корректного добавления в бд
        """

        for key, value in excel_read_file.items():
            if f'Unnamed: 0_level_1' in key or f'Unnamed: 1_level_1' in key:
                new_key = key[0]
                self.new_dict[new_key] = value
            else:
                new_key = '_'.join(key)
                self.new_dict[new_key] = value
        return self.new_dict




conn = psycopg2.connect(database="postgres", user="postgres", password="root", host="localhost", port="5432")
cur = conn.cursor()


def create_table(table_name_us: str, new_dict: dict):
    """
    Проводим проверку вхождения названия таблицы, если таблицы нет в схеме, создаем её
    и добавляем стобцы.
    """

    create_tables_query = f"""CREATE TABLE {table_name_us} (id VARCHAR(64))"""

    def create_colums_query(new_dict: dict):
        """
        Заполняем оставшиеся в таблице столбцы по ключам из словаря.
        """
        o = 1

        for i in new_dict.keys():
            if i == 'id':
                pass
            elif i[:-2] == 'Unnamed:':
                cur.execute(f"""ALTER TABLE {table_name_us} ADD {i[:-3]}{str(o)} VARCHAR(64)""")
                o += 1
                conn.commit()
            else:
                cur.execute(f"""ALTER TABLE {table_name_us} ADD {i} VARCHAR(64)""")
                conn.commit()

    try:
        cur.execute(create_tables_query)
        create_colums_query(new_dict)
    except psycopg2.errors.DuplicateTable:
        pass
    finally:
        conn.commit()

def update_columns_query(new_dict: dict):
    """
    Вносим значения из словаря в бд.
    """
    cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name_us}'")
    column_names = [row[0] for row in cur.fetchall()]

    values_list = []
    for row in new_dict.values():
        row_values = []
        for value in row.values():
            if isinstance(value, (float, np.floating)):
                if np.isnan(value):
                    row_values.append(None)
                else:
                    row_values.append(value)
            else:
                row_values.append(value)
        values_list.append(row_values)

    placeholders = ','.join(['%s'] * len(column_names))
    insert_query = f"INSERT INTO {table_name_us} ({', '.join(column_names)}) VALUES ({placeholders})"

    for values in zip(*values_list):
        try:
            cur.execute(insert_query, values)
        except psycopg2.Error as e:
            print(f"Error inserting row: {e}")
            conn.rollback()
            break
        else:
            conn.commit()


create_a_table_dict(excel_read_file)
create_table(table_name_us, new_dict)
update_columns_query(new_dict)


cur.close()
conn.close()
