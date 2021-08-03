
#objective: itirate over all numbers till the nth prime. ignore even numbers. 
#Success! Horribly Inefficient tho :()

def PrimeCheck(num):
    for x in range(2,num):
        if num % x == 0:  
            return False

            
    return True

        
def PrimeFind(nth):
    if nth == 1:
        return 2
    i=1
    prime_count= 1
    while prime_count < nth:
        i += 2
        if PrimeCheck(i):
            prime_count +=1

    return i
    
print(PrimeFind(10001))






       
         