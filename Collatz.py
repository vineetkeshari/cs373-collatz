#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------

# Cache for storing collatz lengths of seen numbers
collatz_cache = {}

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    if len(l) < 2 :
        return False
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_length
# ------------

def collatz_length (num) :
    """
    returns the length of collatz sequence for a number
    
    num is the number we need the collatz length for
    looks up and adds values to collatz_cache
    """
    assert num > 0

    if num in collatz_cache :
        return collatz_cache[num]
    else :
        if num == 1 :
            length = 1
        else :
            if num % 2 == 0 :
                length = collatz_length (num/2) + 1
            else :
                length =  collatz_length ((num*3 + 1)/2) + 2
        assert length > 0
        collatz_cache[num] = length
        return length

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    return the max cycle length in the range [i, j]
    
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    i and j are swapped if they are in the wrong order
    """
    assert i > 0
    assert j > 0
    if i > j :
        t = i
        i = j
        j = t
    assert i <= j
    
    v = 1
    for num in range (i, j+1) :
        length = collatz_length (num)
        if length > v :
            v = length

    assert v > 0
    return v

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)
