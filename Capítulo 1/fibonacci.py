from functools import lru_cache

def main():
    number = int(input('Number of Fibonacci sequence: '))
    print(fib(number))

@lru_cache(maxsize=None)
def fib(n:int) -> int:
    '''
    Função que mostra o número da sequência fibonacci.
    '''
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

if __name__ == '__main__':
    main()