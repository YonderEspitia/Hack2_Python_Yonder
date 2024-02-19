"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""

result = {"foo":"fookziman","bar":"barziman"}

def fn_hack_9(result):
    final = {}
    for key, value in result.items():
        if key.lower() == 'foo':
            final['Foo'] = value.replace('k', '').capitalize()
    return final


print(fn_hack_9(result))