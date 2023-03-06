
from SimpleStack import *

stack = Stack(50) # Crear los limites de la pila
pa = input("Palabra a invertir: ")

for let in pa: # Cada letra de la palabra se recorre en un bucle for
    if not stack.isFull(): # pone las letras si la pila tiene suficiente espacio
        stack.push(let)

reverb = '' #se crea una cadena de caracteres vacía llamada reverb

while not stack.isEmpty(): #  Luego, se extraen las letras de la pila utilizando el método pop
    reverb += stack.pop()

print('El inverso de ', pa, 'es', reverb)


clean_word = ''.join(e.lower() for e in pa if e.isalpha()) # se limpia la palabra ingresada por el usuario 

for let in clean_word:  
    if not stack.isFull(): 
        stack.push(let)

reverb = '' # mismo proceso que antes, toma la ultima palabra guarda y la invierte

while not stack.isEmpty(): # 
    reverb += stack.pop()

# verifica si la palabra es igual
if clean_word == reverb:
    print(pa, 'es un palíndromo.')
else:
    print(pa, 'no es un palíndromo.')
