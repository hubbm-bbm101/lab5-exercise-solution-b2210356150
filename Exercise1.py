#Write a program that asks for a number N as a user input, and calculates the sum of odd numbers,
# and the average of even numbers starting from 1 up to and including N.
N=int(input("please enter a number:"))

odd_sum = 0
even_sum=0
evens=0

if N%2==0:
    for i in range(1,N+1):
        if i%2==0:
            evens+=1
            even_sum = i + even_sum
    print(N, "is an even number and average of even numbers till",N," is ",even_sum/evens)
    
else:
    for i in range(1,N+1):
        if i%2!=0:
            odd_sum = i + odd_sum
    print(N, "is an odd number and sum of odd numbers till",N," is ",odd_sum)
    
    
    
    