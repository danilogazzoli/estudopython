import pymysql.cursors

conexao = pymysql.connect(host='localhost',
                          user='admin',
                          password = '123',
                          db='interacaopython',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)

#cursor = conexao.cursor()

x = 'drop table pessoas;'

#cursor.execute('create table pessoas(nome varchar(30), idade int, endereco varchar(100));')

with conexao.cursor() as cursor:
    cursor.execute(x)

#cursor.close()
#conexao.close()