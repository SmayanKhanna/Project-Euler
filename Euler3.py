#Euler Problem 3: Try from the largest possible prime


#Step 1: Borrowing problem 7

def is_prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def nth_prime(n):
    num_primes = 1
    prime = 2
    num = 3
    while num_primes < n:
        if is_prime(num):
            prime = num
            num_primes += 1
        num += 2
    return prime

def PFactor(num): 
    n=1
    while num / nth_prime(n) != 1:
        if num % nth_prime(n) == 0:
            num = num / nth_prime(n)
        else:
            n += 1
    return nth_prime(n)
   
print(PFactor(600851475143))


                
        

        
        
