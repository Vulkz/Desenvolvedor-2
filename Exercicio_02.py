def fib(n):
    if n == 0: 
        return n
    
    if n == 1:
        return n
    
    n = fib(n-1) + fib(n-2)
    return n


start = 0
numero = 14

while (True):
    if (fib(start) == numero):
        print("O número informado pertence a ordem.")
        break

    if (fib(start) > numero):
        print("O número informado não pertence a ordem.")
        break
    

    start+= 1
 