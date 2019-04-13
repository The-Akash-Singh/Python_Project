# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 02:19:04 2018

@author: hp
"""

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    
    class Meta:
        model = Post
        fields = ('title', 'text',)