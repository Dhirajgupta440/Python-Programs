n=int(input("Enter the number:"))
fact=1
print("The factorial of given number is:")
for i in range(1,n):
    fact+=fact*i
print(fact)