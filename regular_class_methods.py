# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:53:00 2021

@author: Admin
"""
class Volunteers:
    
    raise_amount = 1.04
    no_of_volunteer = 0
    
    def  __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = fname +'.'+ lname + '@'+'gmail.com'
        self.pay = pay
        
        Volunteers.no_of_volunteer += 1
    
    
    def fullname(self):
        return self.fname + ' ' + self.lname
        #return '{} {}'.format(self.fname, self.lname)
        
    def apply_raise(self):
        self.pay = self.pay * self.raise_amount
        return self.pay
    
    @classmethod# alter the functionality of a method to receive class as the fisrt argument instead of self
    def set_raise_amnt(cls, amount):
        cls.raise_amount = amount
        
        
vol1 = Volunteers("Betty", "Makena", 15000)
vol2 = Volunteers("Hill", "Mount", 17000)

Volunteers.set_raise_amnt(1.08)
vol1.set_raise_amnt(1.09)
print(Volunteers.raise_amount)
print(vol1.raise_amount)
print(vol2.raise_amount)

        
