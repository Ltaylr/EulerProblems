from numpy import math

num = 60085147514386
st = ""
def fact(x, st):
    sq = int(math.sqrt(x))
    print(st + str(x))
    st+="  "
    if sq*sq != x:
        lo = sq - 1
        hi = sq + 1
        pr = lo * hi
        while pr != x and lo > 1:
            if pr > x:
                lo-=1
            else:
                hi+=1
            pr = lo*hi
        if lo == 1:
            # found a prime
            return x
    else:
        # is a square number
        return fact(sq, st)

    return max(fact(lo, st),fact(hi, st))

print(fact(num,""))





