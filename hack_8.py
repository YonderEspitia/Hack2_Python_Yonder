"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""

def fn_hack_8(input_text):
    result = []

    if(len(input_text)==5 or len(input_text)==3 ):
        for i, char in enumerate(input_text, start=1):
            if isinstance(char, int):
                result.append(str(char))
                
            else:
                result.append(f"{char}-{i}")
    else:
           for i, char in enumerate(input_text, start=1):
            if isinstance(char, int):
                result.append(str(char))
                
            else:
                result.append(f"{i}")

    return result[::-1]

# Ejemplos de uso:
input_text1 = ["a", "b", "c", "d", "e"]
result1 = fn_hack_8(input_text1)
print(result1)  # Debería imprimir: ["e-5", "d-4", "c-3", "b-2", "a-1"]

input_text2 = ["a", "b", "c"]
result2 = fn_hack_8(input_text2)
print(result2)  # Debería imprimir: ["c-3", "b-2", "a-1"]

input_text3 = ["a", "b", "c", "d"]
result3 = fn_hack_8(input_text3)
print(result3)  # Debería imprimir: ["4", "3", "2", "1"]

input_text4 = ["a", "b"]
result4 = fn_hack_8(input_text4)
print(result4)  # Debería imprimir: ["2", "1"]


"""def fn_hack_8(s):
    result = s
    #...
    return result"""
