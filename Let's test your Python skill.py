#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Exercice 1
for n in range(2000,3201):
    if (n % 7 == 0 and n % 5 > 0):
        print(n)


# In[20]:


#Exercice 2
def factorial(n):
    r = 1
    if(r < 0):
        r = "Error"
    elif(r == 0):
        r = 1
    else:
        for i in range(1,n+1):
            r = r * i
            print(i,"  ",r)
    return r
while True:
    try:
        a = int(input("Enter your factorial number n factorial m  (n): "))
        if(a >= 0):
            break
        print("Enter a positive number")
    except ValueError:
        a = int(input("Please Enter an integer number : "))
print(factorial(a))


# In[23]:


#Exercice 3
dict1 = dict()
while True:
    try:
        a = int(input("Enter an integer number : "))
        break
    except:
        a = int(input("Please Enter an integer number : "))
for i in range(1,a+1):
    dict1[i] = i*i
print(dict1)


# In[33]:


#Exercice 4
def missing_char(str_a,index):
    if(len(str_a) <= 0):
        r = "Error : Not valid a String"
    elif(len(str_a) == 1):
        r = "Error : Please enter a string with more then 1 char"
    elif(index < 0):
        r = "Error : index number should be equal or superior to 0"
    elif(index > len(str_a)-1):
        r = "Error : index should be in range of your string of character length"
    else:
        r =  str_a[:index:] + str_a[index+1::]
    return r

print(missing_char('kitten', 1))
    


# In[42]:


#Exercice 5
import numpy as np
npArray = np.array([[0, 1],[2, 3],[4, 5]])
Array = npArray.tolist()
Array


# In[57]:


#Exercice 6
np1 = np.array([0, 1, 2])
np2 = np.array([2, 1, 0])
np_cov = np.cov(np1,np2)
np_cov


# In[60]:


#Exercice 7
def formula_Q(*D):
    C = 50
    H = 30
    Q = tuple()
    for i in D:
        S = round(pow((2*i*C)/H,1/2))
        Q += (S,)
    return Q
print(formula_Q(100,150,180 ))


# In[ ]:




