n=int(input("Enter  number of integers to input:"))
listed=[]
for i in range(n):
        num=int(input("Enter integers:"))
        if num>100:
                num="over"
        listed.append(num)
print(listed)

