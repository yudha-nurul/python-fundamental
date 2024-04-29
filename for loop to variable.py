

def PL(list_name):
    result = ""
    for name in list_name:
        result += f'''
        add Solid "{name}"
        COPY
        PASTE
        EDIT MOVE
        Z 1
        KEEP
        NOKEEP
        APPLY
        DISMISS
        '''
    return result.strip()

list_name = [23, 25, 35]
x = PL(list_name)
print(x)  # Output dari fungsi PL() disimpan dalam variabel x
