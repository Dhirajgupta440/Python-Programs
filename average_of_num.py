num = int(input("How many numbers: "))
sum = 0
	
for i in range(num):
	    numbers = float(input("Enter number : "))
sum += numbers
avg = sum / num
print("Average of ", num, " numbers is :", avg)
