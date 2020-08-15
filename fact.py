def fact(n):
    '''
    >>> fact(1)
    1
    >>> fact(-2)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(3)
    6
    >>> fact(10)
    3628800
    '''

    if n < 1:
        raise ValueError
    if n == 1:
        return 1
    return n * fact(n - 1)
if __name__ == '__main__':
    import doctest
    doctest.testmod()