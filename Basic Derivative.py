DV = []

Edge = int(input("Enter the max character amount : "))

x = int(input("Type X's value : "))

while Edge > 0:

    Edge -= -1

    nc = float(input("Enter the coefficient : ")) 

    epo = float(input("Enter a exponent : "))

    if epo != 0:
        dv = nc*epo*x**(epo-1)
    else:
        dv = 0

    DV.append(dv)
    result = sum(DV)

print(result)
