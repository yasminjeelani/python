# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:49:18 2019

@author: abdul
"""
import pytest

def fizzbuzz(value):
    return "1"

def test_retvalu1():
    retvalue = fizzbuzz(1)
    assert retvalue == '1'