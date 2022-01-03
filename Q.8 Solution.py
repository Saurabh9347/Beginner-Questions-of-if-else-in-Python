m1 = int(input("Enter marks in English: "))
m2 = int(input("Enter marks in Maths: "))
m3 = int(input("Enter marks in SST: "))
av = (m1 + m2 + m3) / 3
print("Percentage obtained =", av)
if av >= 70 :
    print("Very Good")
else :
    print("Work Hard")