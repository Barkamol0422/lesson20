def s(a, b):
    e = []
    o = []    
    for n in range(a, b + 1):
        sq = n ** 2
        if sq % 2 == 0:
            e.append(sq)
        else:
            o.append(sq)   
    return e, o
a = int(input("Enter the start number: "))
b = int(input("Enter the end number: "))
e, o = s(a, b)
print("Even squared values:", e)
print("Odd squared values:", o)
