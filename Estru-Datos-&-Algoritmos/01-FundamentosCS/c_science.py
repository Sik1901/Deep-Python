from math import ceil, floor


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


decimalToBinary(30)  # 11110


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
    return None
