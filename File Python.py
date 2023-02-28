#!/usr/bin/env python
# coding: utf-8

# ### Veronika Juninda ( 21/474552/PA/20495 )

# In[16]:


get_ipython().system('pip install tbcontrol')


# In[17]:


import sympy
import tbcontrol
from tbcontrol.symbolic import routh

s = sympy.Symbol('s')
K = sympy.Symbol('K')


# In[18]:


# NO 1

print("Nilai Polynomial")
p = 7*s**7 + 3*s**6 + 6*s**5 + 4*s**4 + 5*s**3 + 2*s**2 + s + K
p = sympy.Poly(p, s)
p


# In[19]:


print("Routh Table")
R = routh(sympy.Poly(p, s))
R


# In[20]:


print("Nilai K")
sympy.solve([e > 0 for e in R[:, 0]], K)


# In[21]:


# NO 2

print("Nilai Polynomial")
p = 4*s**4 + 3*s**3 + 2*s**2 +  s + 7
p = sympy.Poly(p, s)
p


# In[22]:


print("Routh Table")
R = routh(sympy.Poly(p, s))
R


# In[23]:


print("Nilai K")
sympy.solve([e > 0 for e in R[:, 0]], K)


# In[ ]:




