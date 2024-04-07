# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# count = 0

# for num in numbers:
#     if num > 0 : count+=1;

# if count == 0: print("There is no number which is Positive");
# print(count)

# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.
# n = 5;
# n = int(input("Enter the value of N"))
# sum_of_even_n_num = 0;

# for n in range(1,n+1):
#     if n % 2==0: sum_of_even_n_num +=n;
    
# print(f'sum of {n} even number {sum_of_even_n_num}')

# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# n = int(input("Enter the number for a table"));
# for i in range(1,10+1):
#     if i ==5:
#         continue;
#     print(f"{n} x {i} = {n*i}")


# 4. Reverse a String
# Problem: Reverse a string using a loop.

# string = "python";
# rev_string = "";
# for char in string:
#     rev_string = char + rev_string;

# print(rev_string)

# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

# string = "python";
# for ch in string:
#     if string.count(ch) == 1: 
#         print("character is ", ch);
#         break; # because of only first non-repeated character

# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

# n = 5;
# fact = 1;
# while n > 0:
#     fact *= n;
#     n-=1;
    
# print(fact)


# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

# while True:
#     n = int(input("Enter number b/w 1 to 10"));
#     if 1 <= n <=10: 
#         print(f"you enter {n} , thanks");
#         break;
#     else: 
#         print("invlaid number , Try again");




# 8. Prime Number Checker
# Problem: Check if a number is prime.

# n = 12;
# is_prime = True;

# if n > 1:
#     for num in range(2,n):
#         if (n % num) ==0:
#             is_prime = False;
#             break;
        
# if is_prime:
#     print(f"{n} is prime number");
# else:
#     print(f"{n} is not a prime number")

# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

# items = ["apple", "banana", "orange", "apple", "mango"]
# unique = set();
# for i in items:
#     if i in unique:
#         print("duplicate item",i);
#         break;
#     unique.add(i)

# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.



import time

wait_time = 1;
max_retries = 5;
attempts = 0;

while attempts < max_retries:
    print(f"attempt {attempts+1} - wait time {wait_time}")
    time.sleep(wait_time);
    wait_time *= 2;
    attempts +=1;
