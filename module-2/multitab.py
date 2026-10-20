#------------------------------------------------------------------------------
# This module defines multitab() a multiplication table generator.
#------------------------------------------------------------------------------
import math
underline = '\033[4m'
reset = '\033[0m'
def multitab(n):
    """Print multiplication table up to n.

    Parameters
    ----------
    n : positive integer scalar

    Returns
    -------
    None
    """
    assert (type(n) is int) and (n > 0), "n must be positive integer"

    ### THIS IS WHERE YOU COME IN
    ### USE AS MANY LINES AS YOU NEED
    ### USE A FOR LOOP OR WHILE LOOP, WHICHEVER YOU LIKE
    ### YOU WILL PROBABLY NEED TO LOOK UP SOME THINGS
    ### YOU WILL DISCOVER A USEFUL OPTIONAL PARAMETER TO THE FUNCTION PRINT()
    length = 2
    if n*n < 10:
        length = 1
    elif n*n < 100:
        length = 2
    elif n*n <  1000:
        length = 3
    

    top = f"{n:{length}.0f}| "
    for i in range(1, n+1):
        top = f"{underline}{top} {i:{length}.0f}"
    line = f"{top}{reset}"

    for i in range(1, n+2):
        print(line)
        line = f"{i:{length}.0f}| "
        for j in range(1, n+1):
            line = f"{line} {i*j:{length}.0f}"
            
    return None

### To run as a utility
if __name__ == '__main__':
    n = int(input("Multiplication table size: "))
    multitab(n)
