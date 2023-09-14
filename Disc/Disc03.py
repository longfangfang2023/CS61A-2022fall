def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n==1:
        return m
    return multiply(m,n-1)+m


def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1 or n == 2:
        return n
    else:
        return n * skip_mul(n - 2)



def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    if n == 2:
        return True

    def helper(i=2):
        if i == n:
            return True
        else:
            if n % i == 0:
                return False
            return helper(i+1)
    return helper()


def hailstone(n,count=1):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    if n==1:
        return count
    elif n % 2 == 0:
        return hailstone(n/2,count+1)
    else:
        return hailstone(3*n+1,count+1)


def merge(n1, n2):
    """Merges two numbers by digit in decreasing order.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    "*** YOUR CODE HERE ***"
    n1_rest, n1_last = n1 // 10, n1 % 10
    n2_rest, n2_last = n2 // 10, n2 % 10

    if n1==0 or n2==0:
        return n1+n2

    if n1_last >= n2_last :
        return merge(n1, n2_rest)*10 + n2_last
    else:
        return merge(n1_rest,n2)*10 + n1_last


