
"""3bi"""
import time
#==============================================

#Iteration version of Fibonacci

start = time.time()
# Fibonacci series will start at 0 and travel upto below number
def iter_fabo(Number):
    print("Iterative Fibonacci sequence:")
    # Initializing First and Second Values of a Series
    i = 0
    First_Value = 0
    Second_Value = 1

    # Find & Displaying Fibonacci series
    while(i < Number):
               if i <= 1:
                          Next = i
               else:
                          Next = First_Value + Second_Value
                          First_Value = Second_Value
                          Second_Value = Next
               print(Next)
               i = i + 1

iter_fabo(10)
end = time.time()
print(end - start)



# Python program to display the Fibonacci sequence up to n-th term using recursive functions

start = time.time()
def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = 10
if nterms < 0:
   print("Plese enter a positive integer")
else:
   print("Recursive Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))

end = time.time()
print(end - start)

"""3bii"""
'''
For small data set the recursive version performance is better, while for large
data set it took longer time.
Conclusion: Iteration is better used with large data set for the Fibonacci
sequence.
'''

"""3biii"""

def pascal_triangle(n):
    """
    A function to print out the Pascal's triangle. Takes the number of
    rows to print as its input parameter
    """
    a=[]
    for i in range(n):
        a.append([])
        a[i].append(1)
        for j in range(1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j])
        if(n!=0):
            a[i].append(1)
    for i in range(n):
        print("   "*(n-i),end=" ",sep=" ")
        for j in range(0,i+1):
            print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
        print()

pascal_triangle(10)
