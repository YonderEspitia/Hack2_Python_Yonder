"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""

def fn_hack_4(texto):
    # Verifica si la cadena tiene al menos 6 caracteres
    if len(texto) >= 6:
        # Elimina la primera letra
        result = texto[1:]
        # Elimina la última letra
        result = result[:-1]
        return result
    else:
        # Si la cadena tiene menos de 6 caracteres, devuelve la cadena original
        result=texto
        return result

# Ejemplos de uso
print(fn_hack_4("fooziman"))  # Salida: "oozima"
print(fn_hack_4("barziman"))  # Salida: "arzima"
print(fn_hack_4("qux"))       # Salida: "qux"


"""def fn_hack_4(s):
    result = s
    #...
    return result"""
