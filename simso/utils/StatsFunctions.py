"""
Stats functions
"""



def cdf(rand_var):
    sorted_var = sorted(rand_var, key=lambda x:x[0])
    return reduce(lambda (list_pmit,cdf), (y1,y2): (list_pmit + [(y1,cdf + y2)], cdf + y2), sorted_var, ([],0))[0]
