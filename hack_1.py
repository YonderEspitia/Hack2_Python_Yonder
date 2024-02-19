"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""

def fn_hack_1(s):
   
    if len(s) > 2:
       
        primera_letra = s[0].lower()
        
        segunda_letra = s[1].upper()
        
        result= primera_letra  + segunda_letra + s[2:4] + s[4:5].upper() + s[5:]

        return result
    else:
       
        result = s
        return result


print(fn_hack_1("fooziman")) 
print(fn_hack_1("qux"))       
print(fn_hack_1("eq"))       





"""def fn_hack_1(s):
    result = s
    return result"""
