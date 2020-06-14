#grupos e retrovisores
# [@#a-zA-Z0-9] : conjuntos > para quaisquer caracteres
# (abc|def): grupos: encontra um grupo específico abc ou def
import re
from pprint import pprint

texto = '''
<p> Frase 1</p>
<p> Frase 2</p>
<p>Eita</p>
<p> Qualquer Frase 3</p>
<div>Frase 4</div>
'''
tags = re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto)
pprint(tags)

cpf = '145.125.356-54'
print(re.findall(r'([0-9]{3}\.){2}', cpf))
