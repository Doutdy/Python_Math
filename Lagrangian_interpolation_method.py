#coding: utf-8
import sympy as sp

def Lagrange_interpolation(keys, values):
    x = sp.symbols('x')
    t = len(keys)
    ploy = []
    for i in range(t):
        lst = ['((x-'+str(k)+')/('+str(keys[i])+'-'+str(k)+'))' for k in keys if k != keys[i]]
        item = '*'.join(lst)
        ploy.append(str(values[i])+'*'+item)
    ploy = '+'.join(ploy)
    ploy_exp = sp.expand(ploy)
    ploy_fact = sp.factor(ploy_exp)
    return ploy_fact

def degree_of_sum(k):
    xList, yList = [], []
    degree = k
    cul_sum = 0
    for i in range(1, degree+3):
        xList.append(i)



def main():

    x1 = [1, 2, 4]
    y1 = [3, 5, 3]
    if len(x1) != len(y1):
        print('the lengths of two list are not equal!')
    else:
        print('Lagrange interpolation polynomial is:')
        print(Lagrange_interpolation(x1, y1))
if __name__ == '__main__':

    main()

