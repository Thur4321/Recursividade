def potencia(base, expoente):
  if expoente == 0:
    return 1
  else:
    return base * potencia(base, expoente-1)

def somaLoop(a, b):
  i = 1
  while i <= b:
    a += 1
    i += 1
  return a

def somaRecur(a, b):
  if b == 1:
    return a + b
  else:
    return 1 + somaRecur(a, b-1)



def fusc(n, profund):
  i = 0
  while i < profund:
    print('...')
    i+=1
  print('fusc(', n, ', ', profund, ')')
  if n == 1:
    return 1
  elif n%2 == 0:
    return fusc(n/2, profund+1)
  else: 
    return fusc((n-1)/2, profund+1) + fusc((n+1)/2, profund + 1)


def h(m, n):
  if n == 1:
    return m + 1
  elif m == 1:
    return n + 1
  else:
    return h(m, n -1) + h(m-1, n)

def mdc(x, y):
  if x == y:
    return x
  elif x < y:
    return mdc(y, x)
  else:
    return mdc(x - y, y)

def nx(n, x):
  if x == 1:
    return n
  else: 
    return n + nx(n, x - 1)

def impares(n):
  if n == 1:
    return 1
  else:
    return 2*n-1 + impares(n-1)

def mod(n, m):
  if n < m:
    return n
  else:
    return mod(n-m, m)

def fatorial(x):
  if x == 1:
    return 1
  else:
    return x * (fatorial(x-1))

def F(x):
  if x%3 == 0:
    return x*x
  elif x%3 == 1:
    return x+3
  elif x%3 == 2:
    return fatorial(x)

def sum(n):
  if n == 0:
    return 1
  else:
    return 1/(n+1) + sum(n-1)

def sumLess(n):
  if n == 0:
    return 1
  elif n%2 != 0:
    return sumLess(n-1) - 1/(n+1)
  else:
    return sumLess(n-1) + 1/(n+1)
  
def conversor(n):
  if n < 16:
    return n
  else:
    return '', conversor(n//16), (n%16)

def ordenar(lista, inicio):
  if inicio == len(lista)-1:
    return lista
  else:
    pos = inicio
    aux = lista[inicio]
    for i in range(inicio, len(lista)):
      if lista[i] < aux:
        aux = lista[i]
        pos = i
    primeiro = lista[inicio]
    lista[inicio] = aux
    lista[pos] = primeiro
    return ordenar(lista, inicio + 1)


def permutacao(lst): 
    
    if len(lst) == 0: 
        return [] 
    
    elif len(lst) == 1: 
        return [lst] 
    else:
  
      l = [] 
      
      for i in range(len(lst)): 
         m = lst[i] 
         
         remLst = lst[:i] + lst[i+1:] 
         
         for p in permutacao(remLst): 
             l.append([m] + p) 
      return l

def jogo(n, m):
  lst = ['a'] * n + ['b'] * m
  if n == 0 and m == 0:
    return []
  elif n == 0 and m > 0:
    return [lst]
  elif m == 0 and n > 0:
    return [lst]
  else:
    l = []
    for i in range(len(lst)):
      j = lst[i]
      if lst[i] == 'a':
        for p in jogo(n-1, m):
          l.append([j] + p)
      else:
        for p in jogo(n, m-1):
          l.append([j] + p)
    return l

  
def maior(lista, n):
  if n == len(lista) - 1:
    return lista[n]
  else:
    if lista[n] > maior(lista, n+1):
      return lista[n]
    else:
      return maior(lista, n+1)


  
l = ['a', 'b', 'c']
print(permutacao(l))