#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
for i in range(1,11):
    print(i)


# In[2]:


#2
numbers=[1,2,3,4,5,67]
result=0
for i in numbers:
    result +=i
print('the sum of numbers is :',result)


# In[5]:


# 3
word="hello world"
for char in range(len(word)-1,-1,-1):
    print(word[char],end='')
print('\n')


# In[8]:


#4
numbers=5
factorial=1
for i in range(1,numbers + 1):
    factorial *=i
print('factorial of a given number :',factorial)


# In[9]:


#5
n=int(input('enter a number'))
for i in range(1,11):
    print(n,'x',i,'=',n*i)


# In[10]:


#6
count_even=0
count_odd=0
for i in range(10):
    if i % 2 == 0:
        count_even +=1
    elif i % 2 != 0 :
        count_odd +=1
print('total even numbers are :',count_even)
print('total odd numbers are :',count_odd)


# In[11]:


#7
for i in range(1,6):
    square = i ** 2
    print('the square of i is :',square)


# In[13]:


#8
word="hello world"
length=0
for char in word:
    length=length+1
print(length)


# In[15]:


#9
numbers=[1,2,3,4,5,6,7,8]
sum_of_numbers=0
for numb in numbers:
    sum_of_numbers +=1
average=sum_of_numbers/len(numbers)
print("average:",average)


# In[16]:


#10
n=10
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c


# In[17]:


#11
l=[1,2,3,4,5,4,3,2,2,1]
l1=[]
l2=[]
for i in l:
    if i not in l1:
        l1.append(i)
    elif i not in l2:
        l2.append(i)
print(l2)


# In[19]:


#12
start=9
end=60
for num in range(start,end+1):
    if num >1:
        is_prime=True
        for i in range(2,num):
            if (num %i)==0:
                is_prime=False
                break
        if is_prime:
            print(i)


# In[20]:


#13
word="pwskills data science pro"
vowels="aeiouAEIOU"
count=sum(word.count(vowel)for vowel in vowels)
print(count)


# In[24]:


#14
def find_max_2d(lst):
    max_element = float('-inf')
    for row in lst:
        for element in row:
            if element > max_element:
                max_element = element
    return max_element
# Example usage:
matrix = [
[3, 7, 1],
[9, 4, 8],
[2, 5, 6]
]
max_value = find_max_2d(matrix)
print("The maximum element is:", max_value)


# In[25]:


#15
def remove_element(lst, target):
    for item in lst[:]:
        if item == target:
            lst.remove(item)
my_list = [1, 2, 2, 3, 4, 2, 5]
element_to_remove = 2
remove_element(my_list, element_to_remove)
print("List after removing", element_to_remove, ":", my_list)


# In[26]:


#16
for i in range(1, 6):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)


# In[27]:


#17
def fahrenheit_to_celsius(fahrenheit_temperatures):
    celsius_temperatures = []
    for fahrenheit in fahrenheit_temperatures:
        celsius = (fahrenheit - 32) * 5/9
        celsius_temperatures.append(celsius)
    return celsius_temperatures
fahrenheit_temperatures = [32]
celsius_temperatures = fahrenheit_to_celsius(fahrenheit_temperatures)
print("Celsius Temperatures:", celsius_temperatures)


# In[28]:


#18
def common_elements(list1, list2):
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                common.append(item1)
    return common
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements_list = common_elements(list1, list2)
print("Common elements:", common_elements_list)


# In[29]:


#19
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


# In[30]:


#20
def find_gcd(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd
num1 = 48
num2 = 60
gcd = find_gcd(num1, num2)
print("GCD of", num1, "and", num2, "is", gcd)


# In[32]:


#21
def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total
numbers = [123, 45, 678]
digit_sums = [sum_of_digits(num) for num in numbers]
print("Sum of digits for each number:", digit_sums)


# In[33]:


#22
def prime_factors(n):
    factors = []
    for factor in range(2, n + 1):
        if n % factor == 0:
            prime = True
            for d in range(2, factor):
                if factor % d == 0:
                    prime = False
                    break
            if prime:
                factors.append(factor)
    return factors
number = 36
factors = prime_factors(number)
print("Prime factors of", number, "are:", factors)


# In[34]:


#23
l = [1, 2, 2, 3, 4, 4, 5, 5]
l1= []
for element in l:
    if element not in l1:
        l1.append(element)
print("Unique elements:", l1)


# In[36]:


#24
limit=100
palindromic_numbers=[]
for num in range(1,limit + 1):
    if str(num) == str(num)[::-1]:
        palindromic_numbers.append(num)
print("palindromic numbers up to ",limit,"are",palindromic_numbers)


# In[37]:


#25
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = []
for sublist in nested_list:
    for item in sublist:
        flattened_list.append(item)
print("Flattened list:", flattened_list)


# In[38]:


#26
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_sum = 0
odd_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)


# In[39]:


#27
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = {keys[i]: values[i] for i in range(len(keys))}
print("Combined dictionary:", combined_dict)


# In[40]:


#28
text = "Hello, world!"
vowels = [char for char in text if char.lower() in 'aeiou']
print("Vowels in the text:", vowels)


# In[43]:


#29
strings = ["abc123", "def456", "ghi789", "jklmno"]
numeric_strings = [''.join(char for char in s if char.isdigit()) for s in strings]
print("Numeric strings:", numeric_strings)


# In[45]:


#31
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for current in range(2, int(limit**0.5) + 1):
        if sieve[current]:
            for multiple in range(current*current, limit + 1, current):
                sieve[multiple] = False
    return [x for x in range(2, limit + 1) if sieve[x]]
limit = int(input("Enter the limit: "))
prime_list = sieve_of_eratosthenes(limit)
print("Prime numbers up to", limit, "are:", prime_list)


# In[64]:


#32
def generate_pythagorean_triplets(limit):
    triplets = [(a, b, c) for a in range(1, limit) for b in range(a, limit) for c in range(b, limit) if a**2 + b**2 == c**2]
    return triplets
limit = int(input("Enter the limit: "))
pythagorean_triplets = generate_pythagorean_triplets(limit)
print("Pythagorean triplets up to", limit, "are:", pythagorean_triplets)


# In[47]:


#33
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combinations = [(x, y) for x in list1 for y in list2]
print(combinations)


# In[48]:


#34
import statistics
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean = sum(numbers) / len(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)


# In[52]:


#35
def generate_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1] + [triangle[i-1][j] + triangle[i-1][j+1] for j in range(i-1)]+ [1]
        triangle.append(row)
    return triangle

n = int(input("Enter the number of rows for Pascal's triangle: "))
pascals_triangle = generate_pascals_triangle(n)
for row in pascals_triangle:
    print(row)


# In[53]:


#37
sentence = "This is a sample sentence with some long words."
words = sentence.split()
longest_word = max(words, key=lambda word: len(word))
print("Longest word:", longest_word)


# In[55]:


#38
strings = ["hello", "world", "programming", "python", "list", "comprehension"]
filtered_strings = [s for s in strings if sum(1 for char in s if char in"aeiouAEIOU") > 3]
print(filtered_strings)


# In[56]:


#39
digit_sums = [sum(map(int, str(n))) for n in range(1, 1001)]
print(digit_sums)


# In[61]:


#40
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def is_palindrome(n):
    return str(n) == str(n)[::-1]
limit = int(input("Enter the limit:"))
prime_palindromes = [n for n in range(2, limit) if is_prime(n) and is_palindrome(n)]
print(prime_palindromes)


# In[ ]:




