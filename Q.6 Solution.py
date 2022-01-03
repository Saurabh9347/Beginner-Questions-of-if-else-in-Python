cp = int(input("Enter the COST PRICE: "))
sp = int(input("Enter the SELLING PRICE: "))
if cp > sp :
    loss = cp - sp
    print("Loss =", loss)
elif cp == sp :
    print("NO LOSS NO GAIN")
else :
    profit = sp - cp
    print("Profit =", profit)