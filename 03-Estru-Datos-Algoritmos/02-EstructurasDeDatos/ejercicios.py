def nFactorial(n):
    """
    Parameters:
    ----------
    Recibe un numero entero

    Returns:
    --------
    Retorna el factorial del numero entero ingresado
    usando recursion como metodo
    """
    total = 0
    if n <= 1:
        return n
    total += n * nFactorial(n-1)
    return total

def nFibonnacci(n):
    """
    Parameters:
    -------
    Recibe un numero entero el cual es la posicion enesima en la serie,
    n es 0 = 0, n es 1 = fibonnaci1, n es 2 = fibonacci2, n es 3 = fibonacci3...

    Returns:
    --------
    Retorna el valor en la posicion, 1 = 1, 2 = 1, 3 = 2, 4 = 3...
    """
    if n == 0:
        return 0
    if n <= 2:
        return 1
    fibo = nFibonnacci(n - 1) + nFibonnacci(n - 2)
    return fibo

def queque():
    """
    Constuir una cola de la cual tenga metodos con los cuales
    pueda meter y sacar elementos,
    ademas que me devuelva la cantidad de elementos que esta 
    contiene

    Return:
    -------
    Una clase que implementa una cola
    """

    class Queque():
        def __init__(self):
            self.lista = []
            self.long = 0
    
        def enqueque(self, element):
            self.lista.append(element)
            self.long += 1
    
        def dequeque(self):
            self.lista.pop()
            self.long -= 1
        
        def size(self):
            return self.long

    return Queque()
