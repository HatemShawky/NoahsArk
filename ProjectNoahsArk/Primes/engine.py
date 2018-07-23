#primelist=[2]
#limit=(113)
#limit=input("print the prime numbers till what number (up limit) ?\n")
def is_divisible(x,y):
    """ returns true if x is divisble by Y and false if not"""
    if divmod(x,y)[1]==0:
        return True
    else:
        return False

def PrimesLessThan(limit):
    """ Not efficient : loops over all existing primes , takes a max number , returns a list of all prime numbers less than it"""
    primelist=[2]
    for i in range(limit)[2:]: #to exclude zero and one(ignore this just housekeeping)
        counter=0 # counts how many times this number was divisible
        for prime in primelist:
            if is_divisible(i,prime):
                counter+=1
            else:
                pass
        if counter == 0: #not divisible by any prime - But there should be some other ways to exclude divisiblity 
            primelist.append(i)
    return primelist