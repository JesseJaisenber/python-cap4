class Stack(object):
    def __init__(self, size): #constructor, (lista vacia)
        self.__stackList = []
        self.__size = size
        self.__top = -1

    def push(self, item): #agrega un elemento a la pila en el tope. 
        if self.isFull():
            raise Exception('Stack overflow')
        else:
            self.__stackList.append(item)
            self.__top += 1

    def pop(self): #elimina y manda elementos al borde de la pila arroja excepcion si la pila esta vacia
        if self.isEmpty():
            raise Exception('Stack underflow')
        else:
            self.__top -= 1
            return self.__stackList.pop()

    def peek(self): #devuelve el elemento en el tope de la pila sin eliminarlo.
        if self.isEmpty():
            return None
        else:
            return self.__stackList[-1]

    def isEmpty(self):
        return self.__top == -1

    def isFull(self):
        return self.__top == self.__size - 1
    
    def __len__(self): # devuelve el número de elementos en la pila.
        return self.__top + 1
    
    def __str__(self): # Convert stack a texto legile
        ans = "[" # Start with left bracket
        for i in range(self.__top + 1): # Loop through current items
            if len(ans) > 1: # Except next to left bracket, 
                ans += ", " # separate items with comma
            ans += str(self.__stackList[i]) # Add string form of item
        ans += "]" # Close with right bracket
        return ans
