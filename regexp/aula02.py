# meta caracteres: . ^ $ * + ? {} [] \ | ()

import re

texto = '''
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lousy dog.
The quick brown Fox jumps over the lousy Dog.
The quick brown dox jumps over the lousy Dog.
The quick brown dox jumps over the lousy Dooooooooog.
'''

# OU |
print(re.findall(r'fox|dog|lazy', texto))

# . para qualquer caracter com exceção de uma quebra de linha
print(re.findall(r'fox|dog|l...y', texto))

# [] um conjunto de caracteres, pode ser usado o range
print(re.findall(r'[a-zA-z0-9]ox|[Dd]og|l...y', texto))
print(re.findall(r'[a-zA-z0-9]ox|[a-zA-z0-9]og|l...y', texto))

#flag re.I ou re.IGNORE
print(re.findall(r'dOg|FOX', texto, flags=re.IGNORECASE))


