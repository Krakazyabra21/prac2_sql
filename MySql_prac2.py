import pymysql
connecct = pymysql.connect(host='5.183.188.132',
                       user='db_vgu_student',
                       password='thasrCt3pKYWAYcK',
                       database='db_vgu_test',
                       charset='utf8'
                       )
print('Подключено!')
cursor = connecct.cursor()
cursor.execute(' SELECT table_name FROM information_schema.tables;')
data = cursor.fetchall()
for row in data:
    print(row)

table = input('Из какой таблицы вывести данные: ')
cursor.execute(f'SELECT * FROM {table};')
data = cursor.fetchall()
for row in data:
    print(row)

connect.commit()