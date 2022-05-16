#!/usr/bin/env python
# coding: utf-8

# In[6]:


if (2.2*3.6):
    print("true")
else:
    print("false")


# In[28]:


3>4
4.0>3.999
4>4
4>+4
True or False
True and False
not False
(True and False)or False
(2<3 and  3>5) or (10==10)

3.0-1.0!=5.0-3.0
3>4 or(2<3 and 9>10)
4>5 or 3<4 and 9>8
not(4>3 and 100>6)


# In[38]:


pi =3.14159
radius =1
area =pi*(r**2)
print("A:",area)
volume=4/3.0*pi*radius**3
print("V",volume)


# In[42]:


radius=1
for i in range(1001):
    area =3.141592*radius**2
    volume=4/3.0*3.14159*radius**3
    #print(radius,area,volume)
    radius=i+1
print(radius)


# In[46]:


a=3
a=+2.0
print(a)
a==5.0
b=10
c=b>9


# In[5]:


import sys


# In[15]:


sys.maxsize
sys.int_info
a=sys.maxsize+1
print(a);type(a)

sys.float_info


# In[26]:


a=1+2j
#print(a)
a.real#정수의 값
a.imag#소숫점 값
1+2-(3*4/6)**5+7%5+32//3
print(1+2-(3/4*6)**5+7%5+32//3)
# % -- remain value
# // -- not contain remain value(only result)
7%5
32//3

for i in range(1,1001):
    if(i%2==0):
        print(i,"Even Number")


# In[20]:


#type conversion
import sys
int(2.7846)
float(2)
1+20.0

#in place operation
b=2.5 ; b+=0.5 #(b=b+0.5)
print (b)
a=20 ; a%=3 ; #print(a)
#-=, *=, %=, //=,/=,etc....
#boolean data type, Logical expression
q=True
#type(q)
q=3<2 ; #print(q)
#logical operator
    #<,>,<=,>=,==,!=
    #chained comparision - is possible
1<10<100 #1<10 and 10<100 same things!!
x=10 ;x +=10
if(10<x<30):
    print("T")#print it
else:
    print("F")        

#and, or, not operators
1>0 and 5==5
a=50
a<10 or a>90
not 10<=a<=90


# In[25]:


#string 
    #it is...non-scalar object / ordered sequence of character
s="hello world" #
s='hello world'# hello word

print(s)

