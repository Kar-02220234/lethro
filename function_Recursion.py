def sum_of_digits(n):
    if  n < 10:    # base case: if n is single digit number,return n
        return n
    else:       #recursive case: calculate sum of digits
        last_digits = n % 10 # get  the last digit of n
        remaining_digits = n // 10  # get the remaining digit 
        
        return last_digits + sum_of_digits(remaining_digits)# recusive calculated and add remaining digit
    

print(sum_of_digits(123))
    
               