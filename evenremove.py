n=int(input("Enter number of integers to input:"))
listed=[]
for i in range(n):
        num=int(input("Enter Integers:"))
        if num%2!=0:
                listed.append(num)
print(f"New List:{listed}")

