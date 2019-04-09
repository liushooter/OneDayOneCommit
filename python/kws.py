
def f1(a, b, c=0, *args, **kw):
    print('a =', a, ', b =', b, ', c =', c, ', args =', args, ', kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, ', b =', b, ', c =', c, ', d =', d, ', kw =', kw)


print(f1('1', '2', 3, 4,5,6, x="x", y="y"))
# a = 1 , b = 2 , c = 3 , args = (4, 5, 6) , kw = {'x': 'x', 'y': 'y'}


print(f2('1', '2', 3, d="d", x="x", y="y"))
# a = 1 , b = 2 , c = 3 , d = d , kw = {'x': 'x', 'y': 'y'}