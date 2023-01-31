import arraystack

def is_matched(expr):

    lefty = '({['
    righty = ')}]'

    s = arraystack.ArrayStack()

    for c in expr:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c) != lefty.index(s.pop()):
                return False
    return s.is_empty()


if __name__ == '__main__':

    e = 'The cat ( sat { [ on the } mat )  but the end'
    print(is_matched(e))