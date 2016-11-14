#kompilacja z python3
#!/usr/bin/python

from fractions import gcd

def add_frac(frac1, frac2):
    resultl = 0; resultm = 0
    if (frac1[1] == frac2[1]):
        resultl = frac1[0] + frac2[0];
        return [resultl, frac1[1]]
    else:
        resultm = frac1[1] * frac2[1]
        resultl = (frac1[0] * (resultm / frac1[1])) + (frac2[0] * (resultm / frac2[1]))
        fgcd = gcd(resultl, resultm)
        return [int(resultl/fgcd), int(resultm/fgcd)]
    
def sub_frac(frac1, frac2):
    resultl = 0; resultm = 0
    if (frac1[1] == frac2[1]):
        resultl = frac1[0] - frac2[0];
        return [resultl, frac1[1]]
    else:
        resultm = frac1[1] * frac2[1]
        resultl = (frac1[0] * (resultm / frac1[1])) - (frac2[0] * (resultm / frac2[1]))
        fgcd = gcd(resultl, resultm)
        return [int(resultl/fgcd), int(resultm/fgcd)]
    
def mul_frac(frac1, frac2):
    resultl = frac1[0] * frac2[0]
    resultm = frac1[1] * frac2[1]
    return [resultl, resultm]

def div_frac(frac1, frac2):
    resultl = frac1[0] * frac2[1]
    resultm = frac1[1] * frac2[0]
    return [resultl, resultm]

def is_positive(frac):
    ispos = True if (frac[0]*frac[1] >= 0) else False
    return ispos

def is_zero(frac):
    isz = True if (frac[0] == 0) else False
    return isz

def cmp_frac(frac1, frac2):
    sub = sub_frac(frac1, frac2)
    if (is_zero(sub)): 
        return 0
    elif (is_positive(sub)):
        return 1
    else: 
        return -1
    
def frac2float(frac):
    frc = (float(frac[0])/ float(frac[1]))
    return frc
