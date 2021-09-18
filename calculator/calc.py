#! python3
# calc.py - A calculator program

import re
import math

# Imaginary part regex pattern
imx = re.compile(r'([+-]?)\s*?(\d*\.?\d*)i')

# Real part regex pattern
rex = re.compile(r'([+-]?)\s*?(\d*\.?\d*)')

def stringtonum(n):
    '''
    Converts string to tuple having real and imaginary part of a number
    
    n: string (number in formatted text)
    
    Returns tuple (real part, imaginary part)
    '''
    
    # Check if imaginary part exists
    if imx.search(n) != None:
        
        # Extract the imaginary part
        nig = imx.search(n).groups()
        
        # If imaginary part = 1
        if nig[1] == '':
            ni = float(nig[0] + '1')
        # Otherwise
        else:
            ni = float(nig[0] + nig[1])
    
    # Otherwise
    else:
        ni = 0.0
        
    # Remove imaginary part from string
    n = imx.sub('', n)
    
    # Check if real part exists
    if rex.search(n).group() != '':
        
        # Extract real part
        nrg = rex.search(n).groups()
        nr = float(nrg[0] + nrg[1])
        
    # Otherwise
    else:
        nr = 0.0
    
    # Return
    return (nr, ni)

def formatNum(n):
    '''
    Formats complex number into readable format
    
    n: tuple (real part, imaginary part)
    
    Returns string
    '''
    
    # If both real and imaginary parts are zero
    if n[0] == 0 and n[1] == 0:
        res = '0'
        
    # Otherwise if only real part is zero
    elif n[0] == 0:
        res = str(n[1]) + 'i'
        
    # Otherwise if only imaginary part is zero
    elif n[1] == 0:
        res = str(n[0])
        
    # Otherwise if none are zero
    else:
        
        # Check if imaginary part is positive
        if n[1] > 0:
            res = str(n[0]) + ' + ' + str(n[1]) + 'i'
        # Otherwise
        else:
            res = str(n[0]) + ' - ' + str(n[1])[1:] + 'i'
        
    # return formatted text
    return res
    
# Calculate the product of 2 complex numbers
def helper(a, b):
    '''
    Returns the product of 2 complex numbers
    
    a: tuple (real part, imaginary part)
    b: tuple (real part, imaginary part)
    
    Returns tuple (real part, imaginary part)
    '''
    return (round(a[0]*b[0] - a[1]*b[1], 2), round(a[1]*b[0] + a[0]*b[1], 2))

# Calculate the polar form of a complex number
def calcPolar(a):
    '''
    Returns polar form of a complex number
    
    a: tuple (real part, imagniary part)
    
    Returns tuple (radius, angle)
    '''
    r = (a[0] * a[0] + a[1] * a[1])**0.5
    c = a[0]/r
    s = a[1]/r
    
    # If first quadrant
    if s >= 0 and c >= 0:
        angle = math.acos(c)
        
    # Otherwise if second quadrant
    elif s >= 0 and c <= 0:
        angle = math.acos(c)
        
    # Otherwise if third quadrant
    elif s <= 0 and c <= 0:
        angle = -math.acos(c)
        
    # Otherwise if fourth quadrant
    else:
        angle = math.asin(s)
        
    return (r, angle)
    
# Perform addition
def add():
    
    # Take input; Convert to tuple
    at = input('Enter 1st number: ')
    a = stringtonum(at)
    bt = input('Enter 2nd number: ')
    b = stringtonum(bt)
    
    # Calculate result
    res = (round(a[0] + b[0], 2), round(a[1] + b[1], 2))
    
    # Print result
    print('Result = ' + formatNum(res))

# Perform subtraction
def sub():
    
    # Take input; Convert to tuple
    at = input('Enter 1st number: ')
    a = stringtonum(at)
    bt = input('Enter 2nd number: ')
    b = stringtonum(bt)
    
    # Calculate result
    res = (round(a[0] - b[0], 2), round(a[1] - b[1], 2))
    
    # Print result
    print('Result = ' + formatNum(res))

# Perform multiplication
def mult():
    
    # Take input; Convert to tuple
    at = input('Enter 1st number: ')
    a = stringtonum(at)
    bt = input('Enter 2nd number: ')
    b = stringtonum(bt)
    
    # Calculate result
    # (a + bi)(c + di) = (ac - bd) + (bc + ad)i
    res = helper(a, b)
    
    # Print result
    print('Result = ' + formatNum(res))

# Perform division
def div():
    
    # Take input; Convert to tuple
    at = input('Enter 1st number: ')
    a = stringtonum(at)
    bt = input('Enter 2nd number: ')
    b = stringtonum(bt)
    
    # Check if denominator is zero
    if b[0] == 0 and b[1] == 0:
        print('Denominator cannot be zero.')
        return
    
    # Calculate result
    # (a + bi)/(c + di) = (a + bi)(c - di)/(c^2 + d^2)
    negb = (b[0], -b[1])
    denom = b[0]**2 + b[1]**2
    numer = helper(a, negb)
    res = (round(numer[0]/denom, 2), round(numer[1]/denom, 2))
    
    # Print result
    print('Result = ' + formatNum(res))

# TODO
def ex():
    
    # Take input; Convert to tuple
    at = input('Enter base: ')
    a = stringtonum(at)
    bt = input('Enter exponent: ')
    b = stringtonum(bt)
    
    #r = (a[0] * a[0] + a[1] * a[1])**0.5
    radius, angle = calcPolar(a)
    
    # If exponent is not complex
    if b[1] == 0:
            
        f = (math.log(radius), angle)
        p = helper(f, b)
        
        res = (round(math.e**p[0] * math.cos(p[1]), 2), round(math.e**p[0] * math.sin(p[1]), 2))
        
        #angle *= b[0]
        res = (round(radius**b[0] * math.cos(b[0] * angle), 2), round(radius**b[0] * math.sin(b[0] * angle), 2))
        
        
        
            
    # Otherwise if exponent is complex
    
    # Calculate result
    # (a + bi)(c + di) = (ac - bd) + (bc + ad)i
    # res = (round(a[0]*b[0] - a[1]*b[1], 2), round(a[1]*b[0] + a[0]*b[1], 2))
    
    # Print result
    print('Result = ' + formatNum(res))

def sqroot():
    
    # Take input; Convert to tuple
    at = input('Enter number: ')
    a = stringtonum(at)
    
    #r = (a[0] * a[0] + a[1] * a[1])**0.5
    radius, angle = calcPolar(a)
    
    res = (round(radius**0.5 * math.cos(0.5 * angle), 2), round(radius**0.5 * math.sin(0.5 * angle), 2))
    
    print('Result = ' + formatNum(res))

# Calculate factorial
def fact():
    
    # Take input; Convert to tuple
    nt = input('Enter a number: ')
    n = stringtonum(nt)
    
    # If number is complex, or negative, or fraction
    if n[1] != 0 or n[0] < 0 or n[0] != int(n[0]):
        print('Cannot calculate factorial.')
    
    # Otherwise
    else:
        f = 1
        for i in range(1, int(n[0] + 1)):
            f = f * i
        res = (f, 0)
        
        # Print result
        print('Result = ' + formatNum(res))
    

# Decide what operation to perform
def calc():
    print('Available operations:')
    print('Press 1 to perform addition')
    print('Press 2 to perform subtraction')
    print('Press 3 to perform multiplication')
    print('Press 4 to perform division')
    print('Press 5 to calculate exponent')
    print('Press 6 to calculate square root')
    print('Press 7 to calculate factorial')
    
    try:
        choice = int(input())
        if choice == 1:
            add()
        elif choice == 2:
            sub()
        elif choice == 3:
            mult()
        elif choice == 4:
            div()
        elif choice == 5:
            ex()
        elif choice == 6:
            sqroot()
        elif choice == 7:
            fact()
        else:
            print('Invalid choice. Please try again.')
    except:
        print('Invalid choice. Please try again.')
        
calc()
