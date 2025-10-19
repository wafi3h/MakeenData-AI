price = float(input ("Enter the price "))
if price > 200:
    dis = price * 0.05
    print(dis)
    
if price <= 10:
        print ("Take it Free")
else:
        print ("No Discount")
        print ("End")
        
a = 2
b = 330
print("A") if a > b else print("B")