from Collatz import collatz_eval

d = {}

for i in range (0,1000) :
    if i == 0 :
        n1 = 1
    else :
        n1 = i * 1000
    n2 = (i+1) * 1000 + 1
    d[i] = collatz_eval (n1, n2)
print d
