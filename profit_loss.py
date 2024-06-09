cp=int(input("The cost price is:"))
sp=int(input("The selling price is:"))
if cp>sp:
    print("loss=",cp-sp)
elif cp<sp:
    print("profit=",sp-cp)
else:
    print("no profit no loss")

