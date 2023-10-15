import time
def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

def extened_nod(a, b):
    print("Расширенный алгоритм евклида")
    start_time = time.perf_counter_ns()
    if(a < b):
        a, b = swap(a, b)
    x , y = 1, 0
    xi, yi = 0, 1
    q = 0
    step = 0
    while 1:
        step += 1
        if (a < b): # свап значений для удобной работы
            a, b = swap(a, b)
        q = a // b
        print(f'step ', step, 'gcd=', b, ' x= ', xi, 'y= ', yi, 'r= ', q)
        if q == a:
            end_time = time.perf_counter_ns()
            elapsed_time = end_time - start_time
            print('Время работы: ', elapsed_time)
            return b, xi, yi
        a -= b * q #вычисление следующего числа а
        if a == 0: # если а = 0 то нод найден
            end_time = time.perf_counter_ns()
            elapsed_time = end_time - start_time
            print('Время работы: ', elapsed_time)
            return b, tmp1, tmp2
        x = x - q * xi  # вычисление х и у
        y = y - q * yi
        tmp1 = x # свап значений для удобной работы
        tmp2 = y
        x, y = xi, yi
        xi = tmp1
        yi = tmp2

def extended_bin_nod(a, b):
    print("Расширенный бинарный алгоритм Евклида")
    start_time = time.perf_counter_ns()
    g = 1
    while a & 1 == 0 and b & 1 == 0:
        a >>= 1
        b >>= 1
        g <<= 1
    u, v, A, B, C, D = a, b, 1, 0, 0, 1
    step = 0
    while u != 0:
        step += 1
        print(f'step ', step, 'a=', u, ' b= ', v, 'x= ', C, 'y= ', D)
        while u & 1 == 0: # пока u четное
            u >>= 1 # деление u на 2
            if A & 1 == 0 and B & 1 == 0: # пока А и В четные деление их на 2
                A >>= 1
                B >>= 1
            else: # иначе
                A = (A + b) >> 1
                B = (B - a) >> 1
        while v & 1 == 0:
            v = v >> 1
            if C & 1 == 0 and D & 1 == 0:
                C >>= 1
                D >>= 1
            else:
                C = (C + b) >> 1
                D = (D - a) >> 1
        if u >= v:
            u -= v
            A -= C
            B -= D
        else:
            v -= u
            C -= A
            D -= B
    d = g * v
    x = C
    y = D
    end_time = time.perf_counter_ns()
    elapsed_time = end_time - start_time
    print(f'step ', step + 1, 'a=', u, ' b= ', v, 'x= ', C, 'y= ', D)
    print('Время работы: ', elapsed_time)
    return d, x, y

def trunc_nod(a, b):
    print("Расширенный алгоритм Евклида с усеченными остатками")
    start_time = time.perf_counter_ns()
    step = 0
    if (a < b):
        a, b = swap(a, b)
    x, y = 1, 0
    xi, yi = 0, 1
    q = 0
    while b > 0:
        q = a // b
        r = a % b
        step += 1
        print('step', step, ': gcd=', b, ' x=', xi, ' y=', yi, ' r=', r)
        if r == 0:
            break
        x = x - q * xi
        y = y - q * yi
        tmp1 = x  # свап значений для удобной работы
        tmp2 = y
        x, y = xi, yi
        xi = tmp1
        yi = tmp2
        if r > (b >> 1):
            r = b - r
            xi = x - xi
            yi = y - yi
        a = b
        b = r
    end_time = time.perf_counter_ns()
    elapsed_time = end_time - start_time
    print('Время работы: ', elapsed_time)
    return b, xi, yi
    # print(f'\ngcd=', b, ' x=', xi, ' y=', yi, '\n')
if __name__ == "__main__":
    # задание 1 - Расширенный алгоритм евклида
    a = 26041023430579436509
    b = 26041025295093363887
    gcd, x, y = extened_nod(a, b)
    print(f"Расширенный алгоритм евклида НОД  равен:\n {gcd}")
    print(f"Коэффициенты x и y  равны:\n {y} и {x}")

    a = 247
    b = 331
    gcd, x, y = extended_bin_nod(a, b)
    print(f"Расширенный бинарный алгоритм Евклида НОД равен\n {gcd}")
    print(f"Коэффициенты x и y  равны: \n{x} и {y}")
    a = 332
    b = 642
    gcd, x, y = trunc_nod(a, b)
    print(f"Расширенный алгоритм Евклида с «усечёнными» остатками НОД равен\n {gcd}")
    print(f"Коэффициенты x и y  равны: \n{y} и {x}")

    c = -9790268047729877235
    d = 9790267346755513864
    f = a * c + d * b
    print(f)