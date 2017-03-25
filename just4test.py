# coding: utf-8


class just4test:
    def __init__(self):
        self.txt = 1

    def __str__(self):
        return str(self.txt)

if __name__ == "__main__":
    st = just4test()
    print st
    print type(st)
