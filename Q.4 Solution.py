a1 = int(input("Enter first angle: "))
a2 = int(input("Enter second angle: "))
a3 = int(input("Enter third angle: "))
if a1 + a2 + a3 == 180 :
    print(a1, "+", a2, "+", a3, "= 180")
    print("Thus, these angles can form a triangle")
else :
    print(a1, "+", a2, "+", a3, "≠ 180")
    print("Thus, these angles cannot form a triangle")