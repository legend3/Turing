def gen():
    for c in 'AB':
        yield c

print(list(gen()))

def gen_new():
    yield from 'AB'

print(list(gen_new()))


# ÍøÉÏÓÃÀı
def one():
    print('one start')
    res = yield from two()
    print('function get res: ', res)
    return 'one' + res


def two():
    print('two start')
    res = yield from three() # 
    return res


def three():
    yield 1
    return 'three'


if __name__ == '__main__':
    gen = one()
    send_1 = gen.send(None)
    print('send_1:', send_1)
    # send_2 = gen.send(None)
    send_2 = next(gen)
    print(send_2)