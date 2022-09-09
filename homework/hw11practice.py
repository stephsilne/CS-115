from cs115 import*



def get():
    n = int(input('gimme n '))
    while True:
        try:
            n = int(input('gimme n '))
            if 1 <= n <= 4:
                return n
            else:
                pass
        except ValueError:
            print('nope')
