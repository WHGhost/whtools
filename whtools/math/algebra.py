def is_prime(n):
    """Tests if a number is prime

    Args:
        n (int): The number to test

    Raises:
        TypeError: If n is not an integer
    """
    if n <= 1:
        return False

    if n == 2:
        return True

    if n%2 == 0:
        return False

    c = 3
    while c**2 <= n:
        if n % c == 0:
            return False
        c += 2
    return True



def primes(*arg):
    """yields the prime numbers between start and stop
    
    Args:
        start (int): only yield primes bigger or equal to start
        stop (int): only yield primes smaller than stop
        
    Yields: The prime numbers
    
    Raises:
        TypeError: If start and stop are not integers or None
    """
    if len(arg) >= 1:
        start = arg[0]
        if len(arg) == 2:
            stop = arg[1]
        else:
            raise TypeError('Too many arguments given')
    else:
        start = 2
        stop = None
    if type(start) != int or type(stop) not in (type(None), int):
        raise TypeError('Invalid argument type')

    n = start

    if n % 2 == 0:
        n += 1

    if start <= 2:
        yield 2

    while stop is None or n < None:
        if is_prime(n):
            yield n
        n += 2
