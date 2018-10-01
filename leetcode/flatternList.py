def flattern(lists, result=[]):
    for item in lists:
        if not isinstance(item, list):
            result.append(item)
        else:
            flattern(item, result)
    return result
    
a = [32,[13,32,[33,2,32],['a','b']],[[['f']]],323,[['r'],['f','vf',43,[12,33]]]]

print(flattern(a))