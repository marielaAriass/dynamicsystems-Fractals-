#!/usr/bin/env python
# coding: utf-8

# In[57]:


#Copyright (C) 2022 marielarojo11@gmail.com

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.


import matplotlib.pyplot as plt
import numpy

def square(x,y,l):
    q1 = (x,y)
    q2 = (x+l,y)
    q3 = (x+l, y+l)
    q4 = (x,y+l)
    ax.plot([q1[0],q2[0],q3[0],q4[0],q1[0]] , [q1[1],q2[1],q3[1],q4[1],q1[1]])
#x,y = (square(0,0,1))
#plt.plot(x,y)
#plt.show()
def fractal(n, x, y, l):
    square(x, y, l)
    if n > 0:
        l1 = l / 3
        a1 = x+l
        a2 = y+l1
        fractal(n-1,a1,a2,l1)
        b1 = x+l1
        b2 = y-l1
        fractal(n-1,b1,b2,l1)
        c1 = x-l1
        c2 = y+l1
        fractal(n-1,c1,c2,l1)
        d1 = x+l1
        d2 = y+l
        fractal(n-1,d1,d2,l1)
fig, ax = plt.subplots()
ax.set_aspect('equal')
fractal(6, 0, 0, 1)
plt.show()


# In[ ]:




