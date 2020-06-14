# meta caracteres: ^ $  ()
# Quantificadores:
# * 0 ou n
# + 1 ou n
#? 0 ou 1
# {min, max}

import re

texto = '''
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lousy dog.
The quick brown Fox jumps over the lousy Dog.
The quick brown dox jumps over the lousy Dog.
The quick brown dox jumps over the lousy Doooooooog.
The quick brown dox jumps over the lousy Dooooooooooogg.
The quick brown dox jumps over the lousy Dg.
'''

# + qualquer quantidade de letra "o" ou "g"
resultado = re.findall(r'dO+g+', texto, flags=re.I) # re.I = re.IGNORE
print(resultado)
print(type(resultado))

# * pega qualquer quantidade mesmo existindo ou nao a letra "o" ou "g"
resultado = re.findall(r'do*g', texto, flags=re.I) # re.I = re.IGNORE
print(resultado)

# {10,} = 10 ou mais
# {,10} até 10

resultado = re.findall(r'do{,2}g*', texto, flags=re.I) # re.I = re.IGNORE
print('{,2}: até duas letras o')
print(resultado)

resultado = re.findall(r'do{10}[g]{0,2}', texto, flags=re.I) # re.I = re.IGNORE
print('{10}: dez letras o')
print(resultado)


