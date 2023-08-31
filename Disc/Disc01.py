def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    if temp < 60 or raining:
        return True
    else:
        return False


def nearest_ten(n):
    """
    >>> nearest_ten(0)
    0
    >>> nearest_ten(4)
    0
    >>> nearest_ten(5)
    10
    >>> nearest_ten(61)
    60
    >>> nearest_ten(2023)
    2020
    """
    "*** YOUR CODE HERE ***"
    a, b = n // 10, n % 10
    if b<=4:
        return a * 10
    else:
        return (a+1)*10

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None # No return value
    True
    """
    "*** YOUR CODE HERE ***"
    for i in range(1,n+1):
        if i % 3 ==0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 ==0 and i % 5 != 0:
            print('fizz')
        elif i % 5 ==0 and i % 3 != 0:
            print('buzz')
        else:
            print(i)


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True

def unique_digits(n):
    """Return the number of unique digits in positive integer n.
    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for k in range(10):
        if has_digit(n,k):
            count +=1
    return count



def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    "*** YOUR CODE HERE ***"
    n = str(n)
    k = str(k)
    if k in n:
        return True
    else:
        return False