#comportamento greedy
import re

texto = '''
<p> Frase 1</p>
<p> Frase 2</p>
<p>Eita</p>
<p> Qualquer Frase 3</p>
<div>Frase 4</div>
'''

#.* => representa qualquer coisa
#o \ para escapar o /
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto))

#o ? faz com que se comporte como greedy
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))

#o ? faz com que se comporte como greedy
print(re.findall(r'<[pdiv]{1,3}>.+<\/[pdiv]{1,3}>', texto))

#o ? faz com que se comporte como greedy
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto))
