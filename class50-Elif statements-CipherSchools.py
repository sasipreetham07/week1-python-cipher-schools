#class:50
age = int(input())
if 0<age<=3:
    print("Free")
elif 3<age<=11:
    print("150")
elif 11<age<=60:
    print("pay $150/-")
else:
    print("250")