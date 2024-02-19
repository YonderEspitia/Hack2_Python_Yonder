"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""
def fn_hack_6(texto):
    # Verifica si la entrada está vacía
    if not texto:
        return ["0"]

    # Crea la salida con números y guiones
    result = []
    for i in range(len(texto)):
        if i % 2 == 0:
            result.append(str(i+1))
        else:
            result.append("-")
       # result.append(str(i + 1))

    return result

# Ejemplos de uso
print(fn_hack_6(["a", "b", "c", "d", "e"]))  # Salida: ["1", "-", "3", "-", "5"]
print(fn_hack_6([]))  # Salida: ["0"]


"""def fn_hack_6(s):
    result = s
    #...
    return result"""
