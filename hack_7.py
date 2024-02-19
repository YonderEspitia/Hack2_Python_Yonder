"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""
   
def fn_hack_7(input_text):
    result = []
    if not input_text:
        return [0]
    else:
        for i, char in enumerate(input_text):
            if isinstance(char, int):
                result.append(char)
            else:
                if (i + 1) % 2 ==0:
                    #result.append((i + 1))
                    result.append((i + 1))
                else:
                    result.append(str(i + 1))


        return result


# Ejemplos de uso:
lista1 = ["a", "b", "c", "d", "e"]
output1 = fn_hack_7(lista1)
print(output1)  # Debería imprimir: ["1", 2, "3", 4, "5"]

lista2 = []
output2 = fn_hack_7(lista2)
print(output2)  # Debería imprimir: [0]


"""def fn_hack_7(s):
    result = s
    #...
    return result"""
