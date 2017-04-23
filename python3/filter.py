'''
Arthor:		StackOverflow
Usage:		Countif that support function and expression as filter
Param:
xs: value list/tuple
fil: filter condition, could be function or expression

Return:		count of element that match condition
'''
def countif(xs, fil):
    count = 0
    for x in xs:
        if callable(fil):
            if fil(x):
                count += 1
        else:
            if fil:
                count += 1
    return count