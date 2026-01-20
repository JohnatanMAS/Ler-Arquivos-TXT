arql = open ('arquivos/estudar.txt', 'r') # r = read
print(arql.read())
print('possui', arql.tell(), 'caracteres')
print(arql.seek(0, 0), 'caracteres lidos')
print(arql.read(7), 'caracteres lidos')
print()

