#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
for i in range(1,50):
    print(i*i)


# In[ ]:


#q2
import random
y = int(input("Enter lower limit: "))
z = int(input("Enter upper limit: "))
x = [(random.randint(y,z)) for x in range (10)]
print (x)


# In[ ]:


def get(x):
    print(x) 
get(x)
Sum = sum(x)
print(Sum)
product = np.prod(x)
print(product)


# In[ ]:


#q4
def collatz(number):

    if number % 2 == 0:
        result = number // 2
        print(result)
        return result

    elif number % 2 != 0:
        value = 3 * number + 1
        print(value)
        return value

x = input("Give me a number: ")
while x != 1:
    x = collatz(int(x))

