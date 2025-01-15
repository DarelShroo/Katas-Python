"""
1. Suma de Números en un Rango

Enunciado:
Escribe una función sumAllNumbers() que devuelva la suma de todos los números en el rango de 00 a 44 (excluyendo 44). Utiliza el rango de Python para hacerlo.

Por ejemplo:

    La suma de 0+1+2+30+1+2+3 es 66.
"""
#Ejercicio 1
def sumAllNumbers(limit: int):
    return sum(range(0, limit+1))


# Tests
def test_sumAllNumbers():
    assert sumAllNumbers(5) == 15  # 1 + 2 + 3 + 4 + 5 = 15
    assert sumAllNumbers(10) == 55  # 1 + 2 + ... + 10 = 55
    assert sumAllNumbers(1) == 1  # Solo 1
    assert sumAllNumbers(0) == 0  # Sin números que sumar
    assert sumAllNumbers(100) == 5050  # Suma de 1 a 100







"""
2. Conteo de Caracteres

Enunciado:
Escribe una función count(s: str) que reciba una cadena de caracteres ss y devuelva un diccionario donde las claves son los caracteres únicos en ss, y los valores son la cantidad de veces que aparecen en la cadena.

Por ejemplo:

    Para la entrada "aabc", el resultado es {'a': 2, 'b': 1, 'c': 1}.
    Para la entrada "abcabc", el resultado es {'a': 2, 'b': 2, 'c': 2}.
"""
#Ejercicio 2
def count(s: str):
    return {a: sum(1 for x in s if x == a is not None) for a in s}
    

#Tests
def test_count():
    assert count("aabc") == {'a': 2, 'b': 1, 'c': 1}
    assert count("abcabc") == {'a': 2, 'b': 2, 'c': 2}
    assert count("a") == {'a': 1}
    assert count("") == {}
    assert count("aaaa") == {'a': 4}








"""
3. Número Narcisista

Escribe una función narcissistic(value: int) que determine si un número entero es un número narcisista. Un número narcisista es aquel que es igual a la suma de sus dígitos elevados a la potencia del número total de dígitos.

Por ejemplo:

    153=13+53+33153=13+53+33, por lo que es narcisista.
    9474=94+44+74+449474=94+44+74+44, también es narcisista.
    123123, no es narcisista.
"""
#Ejercicio 3
def narcissistic(value: int):
    return value == sum([int(a) ** len(str(value)) for a in str(value)])

#Tests
def test_narcissistic():
    assert narcissistic(153) == True
    assert narcissistic(9474) == True
    assert narcissistic(123) == False
    assert narcissistic(370) == True
    assert narcissistic(0) == True


"""
Ordena los Pesos
Descripción:

Tu tarea es ordenar una lista de números representados como cadenas de acuerdo con los siguientes criterios:

    Peso del número:
        El peso de un número se define como la suma de sus dígitos. Por ejemplo:
            El peso de '56' es 5 + 6 = 11.
            El peso de '65' es 6 + 5 = 11.

    Orden lexicográfico:
        Si dos números tienen el mismo peso, deben ordenarse alfabéticamente como cadenas (orden lexicográfico). Por ejemplo:
            '100' viene antes que '123' porque lexicográficamente '100' < '123'.
Entrada:

Una cadena de números separados por espacios. Por ejemplo:
"103 123 4444 99 2000"

Salida:

Una cadena de números ordenados por peso, con los mismos separados por un espacio. Por ejemplo:
"2000 103 123 4444 99"

Ejemplos:

order_weight("103 123 4444 99 2000") # "2000 103 123 4444 99"
order_weight("56 65 74 100 99 68 86 180 90") # "100 180 90 56 65 74 68 86 99"
order_weight("") # ""

Completa la función order_weight para que pase las pruebas dadas. Asegúrate de manejar casos borde como:

    Una cadena vacía ("").
    Números con el mismo peso.
    Números muy grandes.

"""
#Ejercicio 4
def order_weight(s: str):
    pass

    
def test_order_weight():
    assert order_weight("103 123 4444 99 2000") == "2000 103 123 4444 99"
    assert order_weight("2000 10003 1234000 44444444 9999 11 11 22 123") == "11 11 2000 10003 22 123 1234000 44444444 9999"
    assert order_weight("") == ""

    
"""
Ejercicio 5
 Búsqueda de un Patrón con Boyer-Moore
Enunciado:

Escribe una función boyer_moore() que implemente la búsqueda de un patrón en un texto, utilizando el algoritmo Boyer-Moore. La función debe devolver True si el patrón se encuentra en el texto, y False si no es así.
boyer_moore('azucar', 'uc')  # Salida: True
boyer_moore('azucar', 'pan')  # Salida: False
"""

def boyer_moore(text: str, txtsearch: str):
    pass

# Tests
def test_boyer_moore():
    assert boyer_moore('azucar', 'uc') == True 
    assert boyer_moore('azucar', 'pan') == False
    assert boyer_moore('azucar', 'azu') == True
    assert boyer_moore('azucar', 'car') == True
    assert boyer_moore('azucar', 'azucar') == True
    assert boyer_moore('azucar', '') == True
    assert boyer_moore('', 'uc') == False
    assert boyer_moore('abcabcabc', 'abc') == True
