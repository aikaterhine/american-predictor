#!/usr/bin/env python
# coding: utf-8

# In[1]:
import os

def bump_version():
    os.system('bumpversion major version/version.bumpversion.cfg')
    
# In[ ]: