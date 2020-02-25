def compute_hcf(x, y):
    if x > y:
        smaller = x
    else:
        smaller = y
    for i in range(1, smaller + 1):
        if(x % i == 0) and (y % i == 0):
            hcf = i
    return hcf
x = int(input("enter a number: "))
y = int(input("enter a number: "))
print("the H.C.F is",compute_hcf(x, y))