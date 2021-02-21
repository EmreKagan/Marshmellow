DF = []

Edge = int(input("Enter the max character amount : "))

x = int(input("Type X's value : "))

while Edge > 0:

    Edge -= -1

    nc = float(input("Enter the coefficient : ")) 

    epo = float(input("Enter a exponent : "))

    if epo != 0:
        df = nc*epo*x**(epo-1)
    else:
        df = 0

    DF.append(df)
    result = sum(DF)

print(result)
