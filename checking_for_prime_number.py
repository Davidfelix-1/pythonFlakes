def check_prime(n):
   if n >=1:

    for x in range(2, int( n /2 ) +1, 1):
        if (n % x) == 0:
            return(f"{n} is not a prime number. ")
        else:
            return(f'{n} is a prime number. ')

    else:
        print(f"{n} is not a prime number.  ")




print(check_prime(67))
print(check_prime(16))
print(check_prime(48))
