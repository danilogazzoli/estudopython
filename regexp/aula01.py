import re

#findall:
#search: vai retornar o objeto match
#sub: para substituir
#compile: compilar expressões regulares (reutilizar expressões)

string = 'Este é um teste de expressões regulares teste.'
# sem compile
print(re.search(r'teste', string)) #o r faz com que se evite de escapar muitas barras para determinar um path, por exemplo
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'TESTE', string, count=1)) #count para dizer que quantas vai substituir ao encontrar

# com compile
regexp = re.compile(r'teste')
print(regexp.search(string)) #o r faz com que se evite de escapar muitas barras para determinar um path, por exemplo
print(regexp.findall(string))
print(regexp.sub('TESTE', string, count=1)) #count para dizer que quantas vai substituir ao encontrar





