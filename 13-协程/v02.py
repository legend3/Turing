
def simple_coroutine(a):
    print('-> start')

    b = yield a
    print('-> recived', a, b)

    c = yield a + b
    print('-> recived', a, b, c)

# runc
sc = simple_coroutine(5)

aa = next(sc) # 5 -> a
print(aa)
bb = sc.send(6) # 6 -> b
print(bb)
cc = sc.send(7) # 7 -> c
print(cc)

