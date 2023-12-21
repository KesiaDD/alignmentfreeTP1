# https://gist.github.com/amano41/4d254198333d890e6ef7ba622923e87c 
def xorshift128():
    '''xorshift
    https://ja.wikipedia.org/wiki/Xorshift
    '''

    x = 123456789
    y = 362436069
    z = 521288629
    w = 88675123

    def _random():
        nonlocal x, y, z, w
        t = x ^ ((x << 11) & 0xFFFFFFFF)  # 32bit
        x, y, z = y, z, w
        w = (w ^ (w >> 19)) ^ (t ^ (t >> 8))
        return w

    return _random


def main():

    r = xorshift128()

    for i in range(10):
        print(r())


if __name__ == '__main__':
    main()
