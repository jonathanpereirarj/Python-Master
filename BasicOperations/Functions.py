'''
Created on 26 de jul de 2019

@author: JPereira3
'''

def test (number):
    number = 42
    return number
    
def car_rental_cost (days):
    if (days > 7):
        return (days*40) - 50
    elif (days > 3):
        return (days*40) - 20