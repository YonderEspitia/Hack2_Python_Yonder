"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""
def fn_hack_10(lista):
    result = []
    count = 1
    for item in lista:
        new_lista= {}
        for key, value in item.items():
            new_lista[str(count)] = str(count + 1)
            count += 2
        result.append(new_lista)
    return result


original_lista = [{"a": "b"}, {"c": "d"}, {"e": "f"}]
result = fn_hack_10(original_lista)
print(result)


"""def fn_hack_10(s):
    result = s
    #...
    return result"""
