# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 11:36:14 2018

@author: hp
"""

import re

patterns=['term1','term2'] 

text="This is a string with term1, but not have the other term"

for i in patterns:
    print("Search for '%s' in '%s' " %(i, text))
    
    if re.search(i, text):
        print('\n')
        print('Match was found \n')
        
    else:
        print('\n')
        print('No Match was found \n')
        