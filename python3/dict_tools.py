'''
Arthor:		FGO
Usage:		Find positions of value in dict
Return:		Position of value as a list
Example:
temp = find(src_list)
result = temp('test')[0] # which means get the first position of value which include string "test" only
'''
def find(src):
    def body(target):
        return [i for i, x in enumerate(src) if target in x]

    return body



