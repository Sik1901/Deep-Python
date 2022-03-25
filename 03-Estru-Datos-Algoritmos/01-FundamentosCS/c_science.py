from math import floor


def decimalToBinary(decimal):
    """ 
    Parameters
    ----------
    decimal:int
      Recibe un numero decimal (ej: 12)

    Returns
    -------
    binary:str
      Devuelve un numero en binario producto de la conversion de un numero decimal
    """
    binary = ''
    div = decimal
    while (div > 0):
        if div % 2 == 0:
            binary += '0'
        else:
            binary += '1'
        decimal /= 2
        div = floor(decimal)
    return binary[::-1]


def binaryToDecimal(binary):
    """
    Parameters
    ----------
    binary:str
      Numero en binario

    Returns
    ----------
      devuelve un numero entero resultado de convertir un numero binario
    """
    bin = binary[::-1]
    decimal = 0
    exp = 0
    for n in bin:
        if n == '1':
            decimal += (2 ** exp)
        exp += 1
    return decimal
