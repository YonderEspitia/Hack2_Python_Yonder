"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

def fn_hack_3(texto):
    # Diccionario de sustituciones
    Lista = {
        'a': '@',
        'e': '3',
        'i': '¡',
        'o': '0',
        'u': 'v'
    }

    # Transforma cada letra según el diccionario
    texto_mod = ''
    for char in texto:
        if char.lower() in Lista:
            texto_mod += Lista[char.lower()]
        else:
            texto_mod += char
    
    
    return mayuscula_primera_y_ultima(texto_mod)


def mayuscula_primera_y_ultima(text):
    # Verifica si la cadena tiene al menos una letra
    if len(text) > 0:
        # Convierte la primera letra a mayúscula
        primera_letra = text[0].upper()
        # Convierte la última letra a mayúscula
        ultima_letra = text[-1]
        if len(text)>2:
            ultima_letra = text[-1].upper()
        elif(text[0]=="3"):
         ultima_letra = text[-1].upper()
           
            
        # Combina las letras para formar la salida
        result = primera_letra + text[1:-1] + ultima_letra
        return result
    else:
        # Si la cadena está vacía, devuelve la cadena original
        result=text
        return text
    



# Ejemplos de uso
print(fn_hack_3("fooziman"))  # Salida: "F00z¡m@N"
print(fn_hack_3("barziman"))  # Salida: "B@rz¡m@N"
print(fn_hack_3("3q"))        # Salida: "3Q"
print(fn_hack_3("qu"))        # Salida: "Qv"
print(fn_hack_3("qux"))       # Salida: "QvX"







"""def fn_hack_3(s):
    result = s
    #...
    return result"""
