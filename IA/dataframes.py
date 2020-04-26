import pandas as pd

data = { 'Alunos' : ['caio', 'jorge','danilo', 'maria','jose', 'fernando', 'ricardo', 'francisco'],
        'Idade': [15,18,20,25,18,15,19,40],
        'Nota': [8,9,8,9,6,9,8,7]
        }


df = pd.DataFrame(data, columns = ['Alunos', 'Idade', 'Nota'])

df.describe()

df = df.drop([0,1])

df.drop('Idade', axis=1)

df.count()

df.columns

df.shape

df.min()

df['Nota'].min()

df['Nota'].mean()

df.median()

df.sum()

df['Nota'].add(10)

xf = df['Nota'].sub(1)

xf = df['Nota'].mul(2)

xf = df['Nota'].div(3)

nota = df['Nota'][1]

df.loc[df['Nota'] <= 8]

df.loc[df['Idade'] == 18]

# arquivo servicos.csv

df = pd.read_csv('~/Área de Trabalho/estudopython/IA/servicos.csv')

df.describe()

df.columns()

df.count()


#Returns a list of the results after applying the given function  
#to each item of a given iterable (list, tuple etc.) 

def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 

result = map(addition, numbers) 

print(list(result)) 


#Python Closure:

def func1():  #Outer function
  msg = 'eu pertenço à função func1'
  def func2(): #Nested function
      print (msg)
  return func2


obj = func1()  #binding the function to an object
obj()

del func1  #deleting the outer function

func1()   #this returns error as the function is deleted

obj()

#As you can see in above example, even when the outer function is deleted the object still stores and binds the variable msg to inner nested function. This is called closure in Python.

## Closures provide some sort of data hiding as they are used as callback functions. This helps us to reduce the use of global variables.
## Useful for replacing hard-coded constants
## Closures prove to be efficient way when we have few functions in our code.

#end Python Closure.


