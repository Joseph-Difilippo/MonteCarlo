# You will need some import statements up here.
import random
import math
from multiprocessing import Pool
from timeit import timeit

# Student Name: Joseph Difilippo

def piMonteCarlo(n) :
    """Computes and returns an estimation of pi
    using Monte Carlo simulation.

    Keyword arguments:
    n - The number of samples.
    """
    summation = 0
    for i in range(n):
        U = random.random()
        summation += math.sqrt(1 - U**2) 
    pi = (4/n)*(summation)
    return pi
    
def piParallelMonteCarlo(n, p) :
    """Computes and returns an estimation of pi
    using a parallel Monte Carlo simulation.

    Keyword arguments:
    n - The total number of samples.
    p - The number of processes to use.
    """
   
    with Pool(p) as pool:
        tasks = int(n/p) # number of tasks to be evenly ditributed to each processor
        results = [pool.apply_async(piMonteCarlo, [tasks]) for i in range(p)]
        piSum = 0
        for f in results:
            piSum += f.get()
        pi = piSum/p
        return pi
    
def generateTable() :
    """This function should generate and print a table
    of results to demonstrate that both versions
    compute increasingly accurate estimations of pi
    as n is increased.  It should use the following
    values of n = {12, 24, 48, ..., 12582912}. That is,
    the first value of n is 12, and then each subsequent
    n is 2 times the previous.  The reason for starting at 12
    is so that n is always divisible by 1, 2, 3, and 4.
    The first
    column should be n, the second column should
    be the result of calling piMonteCarlo(n), and you
    should then have 4 more columns for the parallel
    version, but with 1, 2, 3, and 4 processes in the Pool."""
    nmax = 12582912
    i = 12
    print('{0:8}\t{1:9}\t{2:9}\t{3:9}\t{4:9}\t{5:9}'.format("N","Seq","P1","P2","P3","P4"))
    while i <= nmax :
        seq = piMonteCarlo(i)
        p1 = piParallelMonteCarlo(i, 1)
        p2 = piParallelMonteCarlo(i, 2)
        p3 = piParallelMonteCarlo(i, 3)
        p4 = piParallelMonteCarlo(i, 4)
        print('{0:8}\t{1:.6f}\t{2:.6f}\t{3:.6f}\t{4:.6f}\t{5:.6f}'.format(i,seq,p1,p2,p3,p4))
        i *= 2

def time() :
    """This function should generate a table of runtimes
    using timeit.  Use the same columns and values of
    n as in the generateTable() function.  When you use timeit
    for this, pass number=1 (because the high n values will be slow)."""
    nmax = 12582912
    num = 1
    i = 12
    print('{0:8}\t{1:9}\t{2:9}\t{3:9}\t{4:9}\t{5:9}'.format("N","Seq","P1","P2","P3","P4"))
    while i <= nmax :
        L = [ random.randint(1,10) for x in range(i) ]
        seq = timeit(lambda : piMonteCarlo(i), number=num)  
        p1 = timeit(lambda : piParallelMonteCarlo(i, 1), number=num) 
        p2 = timeit(lambda : piParallelMonteCarlo(i, 2), number=num)
        p3 = timeit(lambda : piParallelMonteCarlo(i, 3), number=num) 
        p4 = timeit(lambda : piParallelMonteCarlo(i, 4), number=num) 
        print('{0:8}\t{1:.6f}\t{2:.6f}\t{3:.6f}\t{4:.6f}\t{5:.6f}'.format(i,seq,p1,p2,p3,p4))
        i *= 2
