'''
Arthor:		FGO
Usage:		To generate csv string
Param:
header: the column title in tuple/list
content: csv content in tuple/list
separator: separator of csv

Return:		target csv string
Example:
csv_str = gen_csv(
    (Title, Name, Salary),
    (A, a, 100, B, b, 200, C, c, 300),
)
'''
def gen_csv(header, content, separator=','):
    ret = separator.join(header) + '\n'
    for s in content:
        ret += s + separator
        if (len(s.split(separator))) % len(header) == 0:
            ret += '\n'
    return ret
